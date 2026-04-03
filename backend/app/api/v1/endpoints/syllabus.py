from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from typing import List
from app.db.session import get_db
from app.db.base import Paper, Subject, Topic, Subtopic, Concept
from app.schemas.schemas import PaperSchema, SubtopicSchema, SubtopicContentUpdate, ConceptSchema
from app.services.content_generator import ContentGenerator
import uuid

router = APIRouter()

@router.get("/tree", response_model=List[PaperSchema])
def get_syllabus_tree(exam_id: str = "Group_II", db: Session = Depends(get_db)):
    # Optimized fetching using selectinload to prevent N+1 queries
    query = db.query(Paper).options(
        selectinload(Paper.subjects)
        .selectinload(Subject.topics)
        .selectinload(Topic.subtopics)
    )
    
    if exam_id:
        query = query.filter(Paper.exam_id == exam_id)
    
    papers = query.all()
    return papers

@router.get("/subtopic/{subtopic_id}", response_model=SubtopicSchema)
async def get_subtopic_details(subtopic_id: str, db: Session = Depends(get_db)):
    # Fetch subtopic with full concepts - INSTANT FETCH
    subtopic = db.query(Subtopic).options(
        selectinload(Subtopic.concepts)
    ).filter(Subtopic.id == subtopic_id).first()
    
    if not subtopic:
        raise HTTPException(status_code=404, detail="Subtopic not found")
        
    return subtopic

@router.put("/subtopic/{subtopic_id}/content", response_model=ConceptSchema)
async def update_subtopic_content(
    subtopic_id: str, 
    content_update: SubtopicContentUpdate, 
    db: Session = Depends(get_db)
):
    # Check if subtopic exists
    subtopic = db.query(Subtopic).filter(Subtopic.id == subtopic_id).first()
    if not subtopic:
        raise HTTPException(status_code=404, detail="Subtopic not found")
    
    # Try to find an existing concept for this subtopic
    concept = db.query(Concept).filter(Concept.subtopic_id == subtopic_id).first()
    
    if not concept:
        # Create a new concept if one doesn't exist
        concept = Concept(
            id=uuid.uuid4().hex[:10],
            title=subtopic.title,
            content=content_update.content,
            content_telugu=content_update.content_telugu,
            key_points=[],
            examples=[],
            subtopic_id=subtopic_id
        )
        db.add(concept)
    else:
        # Update existing concept
        concept.content = content_update.content
        concept.content_telugu = content_update.content_telugu
    
    db.commit()
    db.refresh(concept)
    return concept
