import os
import re
from typing import List, Dict, Optional
from sqlalchemy.orm import Session, joinedload
from app.db.base import Topic, Concept, Subtopic, Subject, Paper

class SmartIngestor:
    """Intelligently matches raw, unformatted text to syllabus topics using Smart-Matching 2.0."""
    
    # Mapping Paper Titles to specific files for higher precision
    PAPER_FILE_MAPPING = {
        "PAPER I: GENERAL STUDIES AND GENERAL ABILITIES": ["Arihant GK 2025 - Himexam.txt", "TS_Economy_PE2023-24.txt"],
        "PAPER II: HISTORY, POLITY AND SOCIETY": ["History_of_Telangana.txt", "Indian polity.txt", "Indian society.txt", "Telangana_History_EM.txt"],
        "PAPER III: ECONOMY AND DEVELOPMENT": ["ECONOMY & DEVELOPMENT OF INDIA.txt", "Indian-Economic-and-Development.txt", "TS_Economy_PE2023-24.txt"],
        "PAPER IV: TELANGANA MOVEMENT AND STATE FORMATION": ["STATE FORMATION & TELANGANA MOVEMENTS.txt", "Telangana_Movement_Telangana_History.txt"]
    }

    # Keyword overrides for topics that use different headers in textbooks
    KEYWORD_OVERRIDES = {
        "Events of national/international importance": ["National Activities", "National Events", "International Events", "Current Affairs"],
        "Current affairs: Regional, National, International": ["Current Affairs", "National", "International"],
        "General Science & Applications": ["General Science", "Physics", "Chemistry", "Biology"],
        "Geography of India": ["Geography of India", "Indian Geography"],
        "Geography of Telangana State": ["Geography of Telangana", "Telangana Geography"],
        "Indus Valley Civilization features": ["Indus Valley", "Harappan Civilization"],
        "Preamble, FR, DPSP, Fundamental Duties": ["Preamble", "Fundamental Rights", "Directive Principles"],
    }

    def __init__(self, db: Session, raw_dir: str = "sources/text/"):
        self.db = db
        potential_paths = [
            raw_dir,
            os.path.join("backend", raw_dir),
            "sources/raw_text/",
            os.path.join("backend", "sources/raw_text/")
        ]
        self.raw_dir = next((p for p in potential_paths if os.path.exists(p)), raw_dir)
        self.file_cache = {} # Cache file contents to avoid re-reading

    def _clean_text(self, text: str) -> str:
        """Cleans up raw OCR text and removes noise like stray 'l' and page breaks."""
        text = text.replace("", "").replace("\f", "")
        # 1. Remove common OCR 'l' noise
        text = re.sub(r'^\s*l\s*$', '', text, flags=re.MULTILINE)
        # 2. Remove page numbers like (66), 19-20, Page 5
        text = re.sub(r'\(\d+\)', '', text)
        text = re.sub(r'\b\d+-\d+\b', '', text)
        text = re.sub(r'Page\s*\d+', '', text, flags=re.IGNORECASE)
        # 3. Remove URLs
        text = re.sub(r'\(?www\.[a-z0-9\-\.]+\.(com|in|org|net)\)?', '', text, flags=re.IGNORECASE)
        # 4. Collapse extra newlines
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()

    def _get_file_content(self, filenames: List[str]) -> str:
        """Combines specific file contents into a search buffer."""
        buffer = ""
        for name in filenames:
            if name in self.file_cache:
                buffer += self.file_cache[name]
                continue
            
            path = os.path.join(self.raw_dir, name)
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = self._clean_text(f.read())
                    self.file_cache[name] = content
                    buffer += content
        return buffer

    def run_ingestion(self) -> Dict:
        """Scans corpus and matches content to all database concepts using subject mapping."""
        # Pre-load all files for global fallback if needed
        all_files = [f for f in os.listdir(self.raw_dir) if f.endswith(".txt")]
        global_corpus = self._get_file_content(all_files)
        
        if not global_corpus:
            return {"status": "error", "message": f"No .txt files found in {self.raw_dir}"}
            
        # Get all papers to know the context
        papers = self.db.query(Paper).options(
            joinedload(Paper.subjects)
            .joinedload(Subject.topics)
            .joinedload(Topic.subtopics)
            .joinedload(Subtopic.concepts)
        ).all()
        
        matched_count = 0
        
        print(f"--- Starting Smart-Matching 2.0 (Expert Ingestion) ---")
        
        for paper in papers:
            # Determine which files to search for this paper
            paper_files = self.PAPER_FILE_MAPPING.get(paper.title, all_files)
            paper_corpus = self._get_file_content(paper_files)
            
            for subject in paper.subjects:
                for topic in subject.topics:
                    for subtopic in topic.subtopics:
                        for concept in subtopic.concepts:
                            title = concept.title
                            
                            # 1. SEARCH LOGIC
                            search_terms = self.KEYWORD_OVERRIDES.get(title, [title])
                            best_match_content = ""
                            
                            for term in search_terms:
                                pattern = re.compile(re.escape(term), re.IGNORECASE)
                                # Search in paper-specific corpus first
                                matches = list(pattern.finditer(paper_corpus))
                                if not matches: # Fallback to global corpus
                                    matches = list(pattern.finditer(global_corpus))
                                    
                                if matches:
                                    start_idx = matches[0].end()
                                    # Grab context (4000 chars)
                                    best_match_content = (paper_corpus if matches[0].string == paper_corpus else global_corpus)[start_idx:start_idx + 4500]
                                    break
                            
                            if best_match_content:
                                # Detect Language
                                is_telugu = any('\u0c00' <= char <= '\u0c7f' for char in title) or \
                                            any('\u0c00' <= char <= '\u0c7f' for char in best_match_content[:100])
                                
                                if is_telugu:
                                    concept.content_telugu = best_match_content
                                else:
                                    concept.content = best_match_content
                                
                                matched_count += 1
                                print(f" [MATCH] {paper.title[:15]}... -> {title}")
                                
        self.db.commit()
        return {"status": "success", "matched": matched_count}
