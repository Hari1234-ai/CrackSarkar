import sys
import os

backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(backend_dir)

from app.db.session import SessionLocal, engine
from app.db.base import Base, Paper, Subject, Topic, Subtopic, Concept

def seed_db():
    db = SessionLocal()
    
    print("Clearing existing data...")
    db.query(Concept).delete()
    db.query(Subtopic).delete()
    db.query(Topic).delete()
    db.query(Subject).delete()
    db.query(Paper).delete()
    db.commit()

    print("Seeding massive syllabus dictionary...")

    SYLLABUS = {
        "Group_II": [
            {
                "title": "PAPER I - GENERAL STUDIES & GENERAL ABILITIES",
                "subjects": [
                    {
                        "title": "General Studies",
                        "topics": [
                            {
                                "title": "National, International & General Aspects",
                                "items": [
                                    "Events that hold national & international importance",
                                    "Current affairs happening on regional, national, & international level",
                                    "General Science, its applications, and India’s achievements in Science & Technology",
                                    "Disaster Management - Prevention and Mitigation Strategies & Other Environmental Issues",
                                    "Geography of World, India, and Telangana State",
                                    "India’s History and Cultural Heritage",
                                    "Society, Culture, Heritage, Arts and Literature of Telangana",
                                    "Telangana State Policies",
                                    "Social Exclusion, Rights Issues and Inclusive Policies",
                                    "Logical Reasoning; Analytical Ability and Data Interpretation",
                                    "Basic English"
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "title": "PAPER II - HISTORY, POLITY, & SOCIETY",
                "subjects": [
                    {
                        "title": "Socio-Cultural History",
                        "topics": [
                            {
                                "title": "Ancient & Medieval India",
                                "items": [
                                    "Salient features of Indus Valley Civilization, Society and Culture",
                                    "Early and Later Vedic Civilizations",
                                    "Religious Movements in Sixth Century B.C. - Jainism and Buddhism",
                                    "Socio, Cultural Contribution of Mauryas, Guptas, Pallavas, Chalukyas, Cholas",
                                    "Harsha and the Rajput Age",
                                    "The Advent of Islam and the Establishment of Delhi Sultanate",
                                    "Socio, Cultural Conditions under the Sultanate",
                                    "Sufi and Bhakti Movements",
                                    "The Mughals: Social and Cultural Conditions; Language, Literature, Art and Architecture",
                                    "Rise of Marathas and their contribution to Culture",
                                    "Socio-Cultural conditions in the Deccan under the Bahamanis and Vijayanagara"
                                ]
                            },
                            {
                                "title": "Modern India & Telangana",
                                "items": [
                                    "Advent of Europeans and Rise and Expansion of British Rule",
                                    "Socio-Cultural Policies - Cornwallis, Wellesley, William Bentinck, Dalhousie",
                                    "The Rise of Socio-Religious Reform Movements in the Nineteenth Century",
                                    "Social Protest Movements in India – Jotiba and Savithribai Phule, Ambedkar etc.",
                                    "Socio-Cultural conditions in Ancient Telangana",
                                    "Satavahanas, Ikshvakus, Vishnukundins, Mudigonda and Vemulawada Chalukyas",
                                    "Medieval Telangana - Kakatiyas, Qutub Shahis",
                                    "Socio-Cultural developments: Emergence of Composite Culture",
                                    "Foundation of AsafJahi Dynasty, SalarJung Reforms",
                                    "Rise of Socio-Cultural Movements in Telangana, Peasant Armed Struggle"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "Indian Constitution & Politics",
                        "topics": [
                            {
                                "title": "Constitution & Government",
                                "items": [
                                    "Indian Constitution: Preamble, features, Fundamental Rights & Duties, DPSP",
                                    "Indian Government: Structure, Types of Legislatures, Judicial Review & Activism",
                                    "Distribution of administrative powers between Union and States",
                                    "Powers and Functions of Union and State Governments – President, PM, Governor, CM",
                                    "Rural and Urban Governance (73rd and 74th Amendments)",
                                    "India’s Electoral System - Free and Fair Elections, Political Parties",
                                    "Judicial Activism and Judicial System in India",
                                    "Special Provisions for ST, SC, BC, and other minorities",
                                    "Welfare Mechanism for Enforcement"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "Social Structure & Policies",
                        "topics": [
                            {
                                "title": "Society & Issues",
                                "items": [
                                    "Indian Social Structure: Caste System, Family, Marriage, Religion, Kinship, Tribe",
                                    "Social Issues: Inequality and Exclusion, Casteism, Communalism, Regionalism",
                                    "Social Movements: Tribal, Peasant, Dalit, Environmental, Human Rights",
                                    "Telangana Specific Social Issues: Vetti, Jogini, Devadasi System, Flourosis",
                                    "Welfare Programmes & Social Policies: Affirmative Policies for SC, ST, OBC, Women"
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "title": "PAPER III - ECONOMY & DEVELOPMENT",
                "subjects": [
                    {
                        "title": "Indian Economy & Telangana",
                        "topics": [
                            {
                                "title": "Issues and Challenges",
                                "items": [
                                    "Development & Growth Concepts",
                                    "Economic Growth Measures: National Income",
                                    "Unemployment & Poverty Concepts and Measurement",
                                    "Indian Economy Planning: NITI Aayog, Five Year Plans",
                                    "Telangana Economy in undivided AP (1956-2014)",
                                    "Land Reforms in Telangana",
                                    "Agriculture and Allied Sectors in Telangana",
                                    "Industry and Service Sectors in Telangana",
                                    "Development Dynamics: Regional and Social Inequalities",
                                    "Development and Displacement: Land Acquisition Policy",
                                    "Economic Reforms: Growth, Poverty and Inequalities",
                                    "Sustainable Development Goals"
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "title": "PAPER IV - STATE FORMATION & MOVEMENTS",
                "subjects": [
                    {
                        "title": "Telangana Movement",
                        "topics": [
                            {
                                "title": "The Idea & Mobilisational Phase",
                                "items": [
                                    "Historical Background and features of Telangana",
                                    "Hyderabad Princely State and Mulki Rules",
                                    "Merger of Hyderabad State into Indian Union in 1948",
                                    "1952 Mulki-Agitation",
                                    "Formation of Andhra Pradesh in 1956 and Gentlemen’s Agreement",
                                    "Violation of Safeguards and 1969 Agitation",
                                    "Formation of Telangana Praja Samithi",
                                    "Court Judgements on Mulki Rules & Jai Andhra Movement",
                                    "Six Point Formula 1973 and Presidential Order 1975",
                                    "Rise of Naxalite Movement & Regional Parties in 1980’s"
                                ]
                            },
                            {
                                "title": "Towards Formation (1991-2014)",
                                "items": [
                                    "Public awakening and Civil society organisation",
                                    "Establishment of Telangana Rashtra Samithi",
                                    "Role of Political Parties and Joint Action Committees",
                                    "Cultural Revivalism and Sakalajanula Samme",
                                    "Parliamentary Process and Sri Krishna Committee Report",
                                    "Andhra Pradesh State Reorganization Act 2014"
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        "Group_III": [
            {
                "title": "PAPER I - GENERAL STUDIES & GENERAL ABILITIES",
                "subjects": [
                    {
                        "title": "General Studies",
                        "topics": [
                            {
                                "title": "Core Topics",
                                "items": [
                                    "Current Affairs – Regional, National & International",
                                    "International Relations and Events",
                                    "General Science; India’s Achievements in Science and Technology",
                                    "Environmental Issues; Disaster Management",
                                    "World Geography, Indian Geography, and Geography of Telangana State",
                                    "History and Cultural Heritage of India",
                                    "Society, Culture, Heritage, Arts and Literature of Telangana",
                                    "Policies of Telangana State",
                                    "Social Exclusion, Rights Issues, and Inclusive Policies",
                                    "Logical Reasoning; Analytical Ability and Data Interpretation",
                                    "Basic English"
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "title": "PAPER II - HISTORY, POLITY, & SOCIETY",
                "subjects": [
                    {
                        "title": "History & Polity",
                        "topics": [
                            {
                                "title": "Telangana History & Indian Constitution",
                                "items": [
                                    "Socio-Cultural History: Satavahanas, Kakatiyas, Qutubshahis",
                                    "AsafJahi Dynasty; Nizam-British Relations",
                                    "Socio-cultural and Political Awakening in Telangana",
                                    "Integration of Hyderabad State into Indian Union",
                                    "Evolution of Indian Constitution – Salient Features",
                                    "Fundamental Rights – Directive Principles",
                                    "Distinctive Features of Indian Federalism",
                                    "Union and State Governments",
                                    "Rural and Urban Governance",
                                    "Electoral System & Judicial System in India",
                                    "Indian Social Structure & Social Issues",
                                    "Social Movements & Telangana Specific Social Issues"
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "title": "PAPER III - ECONOMY & DEVELOPMENT",
                "subjects": [
                    {
                        "title": "Indian Economy & Telangana Economy",
                        "topics": [
                            {
                                "title": "Economy, Growth & Development",
                                "items": [
                                    "Growth and Development Concepts",
                                    "Measures of Economic Growth: National Income",
                                    "Poverty and Unemployment",
                                    "Planning in Indian Economy",
                                    "Telangana Economy in undivided AP",
                                    "Land Reforms in Telangana",
                                    "Agriculture and Allied Sectors",
                                    "Industry and Service Sectors",
                                    "Development Dynamics & Regional Inequalities",
                                    "Development and Displacement",
                                    "Economic Reforms & Sustainable Development"
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        "Group_IV": [
            {
                "title": "PAPER I: GENERAL STUDIES",
                "subjects": [
                    {
                        "title": "General Studies",
                        "topics": [
                            {
                                "title": "General Awareness",
                                "items": [
                                    "Current Affairs",
                                    "International Relations and Events",
                                    "General Science in everyday life",
                                    "Environmental Issues and Disaster Management",
                                    "Geography and Economy of India and Telangana",
                                    "Indian Constitution: Salient Features",
                                    "Indian Political System and Government",
                                    "Modern Indian History with a focus on Indian National Movement",
                                    "History of Telangana and Telangana Movement",
                                    "Society, Culture, Heritage, Arts, and Literature of Telangana",
                                    "Policies of Telangana State"
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "title": "PAPER II: SECRETARIAL ABILITIES",
                "subjects": [
                    {
                        "title": "Secretarial Abilities & Reasoning",
                        "topics": [
                            {
                                "title": "Aptitude and Logic",
                                "items": [
                                    "Mental Ability (Verbal and non-verbal)",
                                    "Logical Reasoning (Syllogisms, Analytics)",
                                    "Comprehension & Passage Analysis",
                                    "Re-arrangement of sentences with a view to improving analysis of a passage",
                                    "Numerical and Arithmetical abilities (Ratios, Stats, Operations)"
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

    import hashlib

    # Generate deterministic short IDs
    def make_id(*args):
        return hashlib.md5("_".join(args).encode()).hexdigest()[:10]

    for exam_id, papers in SYLLABUS.items():
        for p_idx, paper_data in enumerate(papers):
            p_id = f"{exam_id}_p{p_idx}"
            paper = Paper(id=p_id, title=paper_data["title"], exam_id=exam_id)
            db.add(paper)
            
            for s_idx, subject_data in enumerate(paper_data["subjects"]):
                s_id = make_id(p_id, str(s_idx))
                subject = Subject(id=s_id, title=subject_data["title"], paper_id=p_id)
                db.add(subject)
                
                for t_idx, topic_data in enumerate(subject_data["topics"]):
                    t_id = make_id(s_id, str(t_idx))
                    topic = Topic(id=t_id, title=topic_data["title"], weightage="High", subject_id=s_id)
                    db.add(topic)
                    
                    for i_idx, item_title in enumerate(topic_data["items"]):
                        subt_id = make_id(t_id, str(i_idx))
                        clean_title = item_title[:100] + ('...' if len(item_title)>100 else '')
                        subtopic = Subtopic(id=subt_id, title=clean_title, topic_id=t_id)
                        db.add(subtopic)
                        
                        c_id = make_id(subt_id, "c1")
                        concept = Concept(
                            id=c_id,
                            title=clean_title,
                            content=f"Detailed study content for: {item_title}. This module encompasses all essential facts, figures, and historical context required for the TSPSC examination.",
                            key_points=["Review core definitions and concepts", "Analyze past year question trends relating to this topic", "Memorize key dates, articles, and formulas"],
                            examples=["Example scenarios and mock questions will be dynamically generated by the AI Module based on your study progress."],
                            subtopic_id=subt_id
                        )
                        db.add(concept)
    
    db.commit()

    # --- SEEDING QUESTIONS (Practice Module) ---
    def add_question(topic_id, q_type, text, options=None, answer="", explanation=""):
        q = Question(
            id=f"q-{uuid.uuid4().hex[:8]}",
            topic_id=topic_id,
            type=q_type,
            question_text=text,
            options=options,
            correct_answer=answer,
            explanation=explanation
        )
        db.add(q)

    # Example: Indian Polity FRs (MCQ, T/F, Matching)
    fr_g2 = db.query(Topic).filter(Topic.id == "top-fr-g2").first()
    if fr_g2:
        add_question(fr_g2.id, "mcq", "Which article defines the 'State'?", ["Art 12", "Art 13", "Art 14", "Art 15"], "Art 12", "Article 12 provides the comprehensive definition used throughout Part III.")
        add_question(fr_g2.id, "true_false", "Fundamental Rights are absolute and cannot be restricted.", None, "False", "FRs are subject to reasonable restrictions.")
        add_question(fr_g2.id, "matching", "Match the Following Articles with their titles:", {"Left": ["Art 14", "Art 17", "Art 18"], "Right": ["Abolition of Titles", "Equality Before Law", "Abolition of Untouchability"]}, '{"Art 14": "Equality Before Law", "Art 17": "Abolition of Untouchability", "Art 18": "Abolition of Titles"}')

    # Example: Logical Reasoning (Group IV)
    logic_g4 = db.query(Topic).filter(Topic.id == "top-logic").first()
    if logic_g4:
        add_question(logic_g4.id, "mcq", "All dogs are animals. All animals have four legs. Therefore, all dogs have four legs.", ["Valid Statement", "Invalid Statement", "No Conclusion", "Partially Valid"], "Valid Statement", "This follows a standard categorical syllogism.")

    db.commit()
    print("Full Database Synced with Questions.")
    db.close()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    seed_db()
