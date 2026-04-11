from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
from .api.v1.api import api_router
from .db.session import engine
from .db.base import Base

# Create database tables
Base.metadata.create_all(bind=engine)

# Auto-seed initial exams if empty (for production migration)
# Self-healing: Auto-seed high-fidelity hierarchy if database is empty
from .db.session import SessionLocal
from .db.base import Paper, Subject, Topic, Subtopic, paper_subject_association

def auto_seed_if_empty():
    db = SessionLocal()
    try:
        # Check for Papers instead of the whole tree for speed
        if db.query(Paper).first():
            return

        print("🚀 [CRITICAL] Database empty. Auto-seeding high-fidelity syllabus...")
        
        # High-level Papers
        papers = [
            Paper(id="P1", title="Paper I - General Studies & General Abilities", exam_id="Group_II", order_index=1),
            Paper(id="P2", title="Paper II - History, Polity & Society", exam_id="Group_II", order_index=2),
            Paper(id="P3", title="Paper III - Economy & Development", exam_id="Group_II", order_index=3),
            Paper(id="P4", title="Paper IV - Telangana Movement & State Formation", exam_id="Group_II", order_index=4),
        ]
        db.add_all(papers)
        db.flush()

        # Paper I: General Studies Section
        gs_section = Subject(id="P1-S1", title="General Studies", order_index=1)
        db.add(gs_section)
        db.flush()
        
        # Link Section to Paper I
        db.execute(paper_subject_association.insert().values(paper_id="P1", subject_id="P1-S1"))

        # Paper I Topics
        p1_topics = [
            "National & International Important Events",
            "Current Affairs (Regional, National & International)",
            "General Science & Applications",
            "India’s Achievements in Science & Technology",
            "Disaster Management (Prevention & Mitigation)",
            "Environmental Issues",
            "Geography (World, India, Telangana)",
            "Indian History & Cultural Heritage",
            "Telangana Society, Culture, Arts & Literature",
            "Telangana State Policies",
            "Social Exclusion, Rights Issues & Inclusive Policies",
            "Logical Reasoning, Analytical Ability & Data Interpretation",
            "Basic English"
        ]
        for idx, title in enumerate(p1_topics, 1):
            t = Topic(id=f"P1-S1-T{idx}", title=title, order_index=idx, weightage="High")
            db.add(t)
            db.flush()
            # Link Topic to Subject
            from .db.base import subject_topic_association
            db.execute(subject_topic_association.insert().values(subject_id="P1-S1", topic_id=t.id))

        # Paper II: Core Sections
        p2_sections = {
            "P2-S1": "History",
            "P2-S2": "Indian Constitution & Politics",
            "P2-S3": "Social Structure & Issues"
        }
        for sid, title in p2_sections.items():
            s = Subject(id=sid, title=title, order_index=1)
            db.add(s)
            db.flush()
            db.execute(paper_subject_association.insert().values(paper_id="P2", subject_id=sid))

        db.commit()
        print("✅ [SUCCESS] Production database self-healed with high-fidelity syllabus.")
    except Exception as e:
        db.rollback()
        print(f"❌ [ERROR] Auto-seed failed: {e}")
    finally:
        db.close()

auto_seed_if_empty()

app = FastAPI(
    title="CrackSarkar API",
    description="Backend for AI-powered CrackSarkar exam preparation platform",
    version="1.0.0"
)

# Set up CORS for all origins (Production Ready)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.get("/")
def read_root():
    return {"message": "Welcome to CrackSarkar API", "status": "online"}

app.include_router(api_router, prefix="/api/v1")
