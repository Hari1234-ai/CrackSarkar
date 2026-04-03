import sys
import os
import hashlib

# Add parent directory to path
backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(backend_dir)

from app.db.session import SessionLocal
from app.db.base import Paper, Subject, Topic, Subtopic, Concept
from app.services.pdf_manager import PDFManager
from pdf_mapping import PDF_MAPPING

from app.services.content_generator import ContentGenerator

async def populate_elaborated_content():
    db = SessionLocal()
    manager = PDFManager()
    generator = ContentGenerator(db)
    
    print("--- Starting Textbook Content Ingestion ---")
    
    # Iterate through structured Groups
    for exam_id, paper_maps in PDF_MAPPING.items():
        for paper_title, book_list in paper_maps.items():
            print(f"Processing {paper_title} for {exam_id}...")
            
            # Find the paper in the DB
            paper = db.query(Paper).filter(Paper.exam_id == exam_id, Paper.title.like(f"%{paper_title}%")).first()
            if not paper:
                continue
            
            for subject in paper.subjects:
                for topic in subject.topics:
                    for subtopic in topic.subtopics:
                        for concept in subtopic.concepts:
                            if not concept.content_telugu or len(concept.content) < 300:
                                print(f"  > Elaborating: {concept.title}...")
                                # This will automatically pick the best book from the library
                                await generator.generate_deep_dive(concept.id, concept.title)
    
    print("--- Content Ingestion Complete ---")
    db.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(populate_elaborated_content())
