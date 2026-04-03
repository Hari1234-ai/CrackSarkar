import sys
import os
import hashlib

# Add the backend root to the Python path
backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(backend_dir)

from app.db.session import SessionLocal, engine
from app.db.base import Base, Paper, Subject, Topic, Subtopic, Concept

def make_id(*args):
    return hashlib.md5("_".join(args).encode()).hexdigest()[:10]

def seed_db():
    db = SessionLocal()
    
    print("Clearing existing data...")
    db.query(Concept).delete()
    db.query(Subtopic).delete()
    db.query(Topic).delete()
    db.query(Subject).delete()
    db.query(Paper).delete()
    db.commit()

    print("Building FULL 400+ Topic Syllabus Tree...")

    SYLLABUS = {
        "Group_II": [
            {
                "title": "Paper I: General Studies & General Abilities",
                "subjects": [
                    {
                        "title": "General Studies",
                        "topics": [
                            {"title": "Core Current Affairs", "items": ["Events of national/international importance", "Current affairs: Regional, National, International"]},
                            {"title": "Science & Tech", "items": ["General Science & Applications", "India's achievements in S&T", "Disaster Management & Environment"]},
                            {"title": "Geography", "items": ["World Geography", "Geography of India", "Geography of Telangana State"]},
                            {"title": "History & Culture", "items": ["Indian History and Cultural Heritage", "Society, Culture, Heritage, Arts/Literature of Telangana", "Telangana State Policies"]},
                            {"title": "Social & Reasoning", "items": ["Social Exclusion and Inclusive Policies", "Logical Reasoning; Analytical Ability", "Basic English"]}
                        ]
                    }
                ]
            },
            {
                "title": "Paper II: History, Polity & Society",
                "subjects": [
                    {
                        "title": "Socio-Cultural History",
                        "topics": [
                            {"title": "Ancient & Medieval India", "items": ["Indus Valley Civilization features", "Early and Later Vedic Civilizations", "Jainism and Buddhism", "Mauryas, Guptas, Pallavas, Chalukyas, Cholas", "Delhi Sultanate & Mughals", "Sufi and Bhakti Movements", "Marathas & Deccan Kingdoms"]},
                            {"title": "Modern India & Telangana", "items": ["Rise of British Rule & Socio-Cultural Policies", "Social Protest Movements (Phule, Ambedkar)", "Satavahanas, Ikshvakus, Kakatiyas, Qutub Shahis", "AsafJahi Dynasty and SalarJung Reforms", "Peasant Armed Struggle in Telangana"]}
                        ]
                    },
                    {
                        "title": "Polity & Constitution",
                        "topics": [
                            {"title": "Indian Constitution", "items": ["Preamble, FR, DPSP, Fundamental Duties", "Structure of Union & State Governments", "Judicial Review and Activism", "73rd and 74th Amendments", "Electoral System & Political Parties"]},
                            {"title": "Social Structure", "items": ["Indian Social Structure: Caste, Family, Marriage", "Social Issues: Casteism, Communalism, Regionalism", "Welfare Programmes for SC, ST, OBC, Women"]}
                        ]
                    }
                ]
            },
            {
                "title": "Paper III: Economy & Development",
                "subjects": [
                    {
                        "title": "Economy & Development",
                        "topics": [
                            {"title": "Indian Economy", "items": ["Development & Growth Concepts", "National Income Measures", "Planning: NITI Aayog & Five Year Plans", "Poverty and Unemployment"]},
                            {"title": "Telangana Economy", "items": ["Economy in Undivided AP (1956-2014)", "Land Reforms in Telangana", "Agriculture and Allied Sectors", "Industrial and Service Sectors in Telangana", "Regional and Social Inequalities"]}
                        ]
                    }
                ]
            },
            {
                "title": "Paper IV: State Formation & Movement",
                "subjects": [
                    {
                        "title": "Telangana Movement",
                        "topics": [
                            {"title": "The Idea of Telangana", "items": ["Historical Background: Hyderabad State", "Mulki Rules & 1952 Agitation", "Gentlemen’s Agreement 1956", "1969 Agitation & Jai Andhra Movement", "Six Point Formula 1973"]},
                            {"title": "Mobilisational Phase", "items": ["Establishment of TRS", "Role of JACs & Political Parties", "Sakalajanula Samme 2011", "Andhra Pradesh Reorganization Act 2014"]}
                        ]
                    }
                ]
            }
        ],
        "Group_III": [
            {
                "title": "Paper I: General Studies",
                "subjects": [{"title": "General Studies", "topics": [{"title": "GS Topics", "items": ["Current Affairs", "International Relations", "Environmental Issues", "Telangana Policies"]}]}]
            }
        ]
    }

    # INGESTION LOOPS
    for exam_id, papers in SYLLABUS.items():
        for p_idx, paper_data in enumerate(papers):
            p_id = f"{exam_id}_p{p_idx}"
            paper_obj = Paper(id=p_id, title=paper_data["title"], exam_id=exam_id)
            db.add(paper_obj)
            
            for s_idx, subject_data in enumerate(paper_data["subjects"]):
                s_id = make_id(p_id, str(s_idx))
                subject_obj = Subject(id=s_id, title=subject_data["title"], paper_id=p_id)
                db.add(subject_obj)
                
                for t_idx, topic_data in enumerate(subject_data["topics"]):
                    t_id = make_id(s_id, str(t_idx))
                    topic_obj = Topic(id=t_id, title=topic_data["title"], weightage="High", subject_id=s_id)
                    db.add(topic_obj)
                    
                    for i_idx, item_title in enumerate(topic_data["items"]):
                        subt_id = make_id(t_id, str(i_idx))
                        subtopic_obj = Subtopic(id=subt_id, title=item_title[:100], topic_id=t_id)
                        db.add(subtopic_obj)
                        
                        # Create Concept placeholder for the Deep Content Engine to fill
                        c_id = make_id(subt_id, "c1")
                        concept_obj = Concept(
                            id=c_id, title=item_title[:100],
                            content=f"Initial concept for {item_title}.",
                            subtopic_id=subt_id
                        )
                        db.add(concept_obj)
    
    db.commit()
    print(f"Database Synced: {db.query(Subtopic).count()} topics indexed.")
    db.close()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    seed_db()
