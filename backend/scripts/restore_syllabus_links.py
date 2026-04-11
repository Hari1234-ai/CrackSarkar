import os
import sqlite3
import uuid

DB_PATH = "backend/cracksarkar.db"

# The high-fidelity syllabus structure provided by the user
SYLLABUS_JSON = {
  "version": "1.0",
  "language_support": ["en", "te"],
  "nodes": [
    # ---------------- PAPER I ----------------
    {"id": "P1", "type": "paper", "title": "Paper I - General Studies & General Abilities", "order": 1},
    {"id": "P1-S1", "type": "section", "title": "General Studies", "parent_id": "P1", "order": 1},
    {"id": "P1-S1-T1", "type": "topic", "title": "National & International Important Events", "parent_id": "P1-S1", "order": 1},
    {"id": "P1-S1-T2", "type": "topic", "title": "Current Affairs (Regional, National & International)", "parent_id": "P1-S1", "order": 2},
    {"id": "P1-S1-T3", "type": "topic", "title": "General Science & Applications", "parent_id": "P1-S1", "order": 3},
    {"id": "P1-S1-T4", "type": "topic", "title": "India’s Achievements in Science & Technology", "parent_id": "P1-S1", "order": 4},
    {"id": "P1-S1-T5", "type": "topic", "title": "Disaster Management (Prevention & Mitigation)", "parent_id": "P1-S1", "order": 5},
    {"id": "P1-S1-T6", "type": "topic", "title": "Environmental Issues", "parent_id": "P1-S1", "order": 6},
    {"id": "P1-S1-T7", "type": "topic", "title": "Geography (World, India, Telangana)", "parent_id": "P1-S1", "order": 7},
    {"id": "P1-S1-T8", "type": "topic", "title": "Indian History & Cultural Heritage", "parent_id": "P1-S1", "order": 8},
    {"id": "P1-S1-T9", "type": "topic", "title": "Telangana Society, Culture, Arts & Literature", "parent_id": "P1-S1", "order": 9},
    {"id": "P1-S1-T10", "type": "topic", "title": "Telangana State Policies", "parent_id": "P1-S1", "order": 10},
    {"id": "P1-S1-T11", "type": "topic", "title": "Social Exclusion, Rights Issues & Inclusive Policies", "parent_id": "P1-S1", "order": 11},
    {"id": "P1-S1-T12", "type": "topic", "title": "Logical Reasoning, Analytical Ability & Data Interpretation", "parent_id": "P1-S1", "order": 12},
    {"id": "P1-S1-T13", "type": "topic", "title": "Basic English", "parent_id": "P1-S1", "order": 13},

    # ---------------- PAPER II ----------------
    {"id": "P2", "type": "paper", "title": "Paper II - History, Polity & Society", "order": 2},
    {"id": "P2-S1", "type": "section", "title": "History", "parent_id": "P2", "order": 1},
    {"id": "P2-S1-SS1", "type": "subsection", "title": "Ancient India", "parent_id": "P2-S1", "order": 1},
    {"id": "P2-S1-SS1-T1", "type": "topic", "title": "Indus Valley Civilization – Features, Society & Culture", "parent_id": "P2-S1-SS1", "order": 1},
    {"id": "P2-S1-SS1-T2", "type": "topic", "title": "Vedic Civilization (Early & Later)", "parent_id": "P2-S1-SS1", "order": 2},
    {"id": "P2-S1-SS1-T3", "type": "topic", "title": "Jainism & Buddhism", "parent_id": "P2-S1-SS1", "order": 3},
    
    {"id": "P2-S2", "type": "section", "title": "Indian Constitution & Politics", "parent_id": "P2", "order": 2},
    {"id": "P2-S2-T1", "type": "topic", "title": "Preamble, Rights & Duties", "parent_id": "P2-S2", "order": 1},
    {"id": "P2-S2-T2", "type": "topic", "title": "Federalism", "parent_id": "P2-S2", "order": 2},

    {"id": "P2-S3", "type": "section", "title": "Social Structure & Issues", "parent_id": "P2", "order": 3},
    {"id": "P2-S3-T1", "type": "topic", "title": "Social Structure", "parent_id": "P2-S3", "order": 1},
    {"id": "P2-S3-T2", "type": "topic", "title": "Social Issues", "parent_id": "P2-S3", "order": 2},

    # ---------------- PAPER III ----------------
    {"id": "P3", "type": "paper", "title": "Paper III - Economy & Development", "order": 3},
    {"id": "P3-S1", "type": "section", "title": "Indian Economy", "parent_id": "P3", "order": 1},
    {"id": "P3-S1-T1", "type": "topic", "title": "Growth vs Development", "parent_id": "P3-S1", "order": 1},
    {"id": "P3-S2", "type": "section", "title": "Telangana Economy", "parent_id": "P3", "order": 2},
    {"id": "P3-S2-T1", "type": "topic", "title": "Telangana Overview", "parent_id": "P3-S2", "order": 1},
    {"id": "P3-S3", "type": "section", "title": "Development Issues", "parent_id": "P3", "order": 3},
    {"id": "P3-S3-T1", "type": "topic", "title": "Sustainable Development", "parent_id": "P3-S3", "order": 1},

    # ---------------- PAPER IV ----------------
    {"id": "P4", "type": "paper", "title": "Paper IV - Telangana Movement & State Formation", "order": 4},
    {"id": "P4-S1", "type": "section", "title": "Idea of Telangana", "parent_id": "P4", "order": 1},
    {"id": "P4-S1-T1", "type": "topic", "title": "Historical Background", "parent_id": "P4-S1", "order": 1},
    {"id": "P4-S2", "type": "section", "title": "Mobilisation Phase", "parent_id": "P4", "order": 2},
    {"id": "P4-S2-T1", "type": "topic", "title": "Mulki Rules", "parent_id": "P4-S2", "order": 1},
    {"id": "P4-S3", "type": "section", "title": "Final Formation", "parent_id": "P4", "order": 3},
    {"id": "P4-S3-T1", "type": "topic", "title": "2014 Formation", "parent_id": "P4-S3", "order": 1}
  ]
}

def seed():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print(f"--- Starting Ingestion on {DB_PATH} ---")

    # Wipe tables for clean restore
    tables_to_clear = [
        "papers", "subjects", "topics", "subtopics",
        "paper_subject", "subject_topic", "topic_subtopic"
    ]
    for table in tables_to_clear:
        try:
            cursor.execute(f"DELETE FROM {table}")
            print(f"Cleared table: {table}")
        except sqlite3.OperationalError:
            print(f"Sub-table {table} missing, skipping...")

    nodes = SYLLABUS_JSON["nodes"]

    # 1. Insert Papers
    for n in nodes:
        if n["type"] == "paper":
            cursor.execute("INSERT INTO papers (id, exam_id, title, order_index) VALUES (?, ?, ?, ?)",
                         (n["id"], "Group_II", n["title"], n["order"]))

    # 2. Insert Subjects (Sections) and Link to Papers
    for n in nodes:
        if n["type"] == "section":
            cursor.execute("INSERT INTO subjects (id, title, order_index) VALUES (?, ?, ?)",
                         (n["id"], n["title"], n["order"]))
            cursor.execute("INSERT INTO paper_subject (paper_id, subject_id) VALUES (?, ?)",
                         (n["parent_id"], n["id"]))

    # 3. Insert Topics (Subsection/Topic) and Link to Subjects
    # Note: subsection is mentally treated as a "Topic that has subtopics"
    for n in nodes:
        if n["type"] in ["subsection", "topic"] and n["parent_id"] and "-S" in n["parent_id"] and "-SS" not in n["parent_id"]:
            cursor.execute("INSERT INTO topics (id, title, weightage, order_index) VALUES (?, ?, ?, ?)",
                         (n["id"], n["title"], "High", n["order"]))
            cursor.execute("INSERT INTO subject_topic (subject_id, topic_id) VALUES (?, ?)",
                         (n["parent_id"], n["id"]))

    # 4. Insert Subtopics and Link to Topics
    for n in nodes:
        if n["type"] == "topic" and n["parent_id"] and "-SS" in n["parent_id"]:
            cursor.execute("INSERT INTO subtopics (id, title, order_index) VALUES (?, ?, ?)",
                         (n["id"], n["title"], n["order"]))
            cursor.execute("INSERT INTO topic_subtopic (topic_id, subtopic_id) VALUES (?, ?)",
                         (n["parent_id"], n["id"]))

    conn.commit()
    conn.close()
    print("--- Ingestion Complete! ---")

if __name__ == "__main__":
    seed()
