from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ConceptBase(BaseModel):
    id: str
    title: str
    content: str
    key_points: List[str]
    examples: List[str]
    completed: bool = False

class ConceptCreate(ConceptBase):
    pass

class ConceptSchema(ConceptBase):
    class Config:
        from_attributes = True

class SubtopicBase(BaseModel):
    id: str
    title: str
    progress: float = 0.0

class SubtopicCreate(SubtopicBase):
    pass

class SubtopicSchema(SubtopicBase):
    concepts: List[ConceptSchema]
    class Config:
        from_attributes = True

class TopicBase(BaseModel):
    id: str
    title: str
    weightage: str # High, Medium, Low

class TopicCreate(TopicBase):
    pass

class TopicSchema(TopicBase):
    subtopics: List[SubtopicSchema]
    class Config:
        from_attributes = True

class SubjectBase(BaseModel):
    id: str
    title: str

class SubjectCreate(SubjectBase):
    pass

class SubjectSchema(SubjectBase):
    topics: List[TopicSchema]
    class Config:
        from_attributes = True

class PaperBase(BaseModel):
    id: str
    title: str

class PaperCreate(PaperBase):
    pass

class PaperSchema(BaseModel):
    id: str
    exam_id: str
    title: str
    subjects: List[SubjectSchema]
    
    class Config:
        from_attributes = True

class DailyTaskBase(BaseModel):
    id: str
    type: str # study, practice, revision, mock_test
    title: str
    description: str
    duration_minutes: int
    completed: bool = False
    topic_id: Optional[str] = None
    paper_id: Optional[str] = None

class DailyTaskCreate(DailyTaskBase):
    pass

class DailyTaskSchema(DailyTaskBase):
    class Config:
        from_attributes = True

class DailyPlanBase(BaseModel):
    date: datetime
    overall_progress: float = 0.0

class DailyPlanCreate(DailyPlanBase):
    pass

class DailyPlanSchema(DailyPlanBase):
    tasks: List[DailyTaskSchema]
    class Config:
        from_attributes = True

class UserProgressBase(BaseModel):
    user_id: str
    item_id: str
    item_type: str
    completed: bool = False
    accuracy: float = 0.0
    time_spent: int = 0
    last_studied: datetime = datetime.utcnow()

class UserProgressSchema(UserProgressBase):
    class Config:
        from_attributes = True
