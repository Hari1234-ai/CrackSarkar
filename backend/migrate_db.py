import os
import sys

# Add the parent directory to sys.path to allow imports from app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import create_engine
from app.db.base import Base, Paper
from app.db.session import SQLALCHEMY_DATABASE_URL

def migrate():
    print(f"Connecting to: {SQLALCHEMY_DATABASE_URL.split('@')[-1]}") # Log host only for safety
    
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

    # Initial Seed for Exams if they don't exist
    from sqlalchemy.orm import sessionmaker
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        # Check if Group II exists
        if not db.query(Paper).filter(Paper.id == "Group_II").first():
            print("Seeding initial exams...")
            exams = [
                Paper(id="Group_II", title="TSPSC Group II", exam_id="Group_II", description="Executive and Non-Executive Posts", order_index=1),
                Paper(id="Group_III", title="TSPSC Group III", exam_id="Group_III", description="Senior Accountant and Auditor Posts", order_index=2),
                Paper(id="Group_IV", title="TSPSC Group IV", exam_id="Group_IV", description="Junior Assistant and Typist Posts", order_index=3),
            ]
            db.add_all(exams)
            db.commit()
            print("Seeding complete.")
        else:
            print("Exams already exist, skipping seed.")
    except Exception as e:
        print(f"Seed error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    if "sqlite" in SQLALCHEMY_DATABASE_URL:
        print("WARNING: You are still connected to SQLite. Please export DATABASE_URL first.")
    migrate()
