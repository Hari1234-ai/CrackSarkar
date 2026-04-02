from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....db.session import get_db
from ....schemas.schemas import DailyPlanSchema
from ....services.plan_service import PlanService

router = APIRouter()

@router.get("/today", response_model=DailyPlanSchema)
def get_today_plan(exam_id: str = "Group_II", user_id: str = "default_user", db: Session = Depends(get_db)):
    return PlanService.generate_daily_plan(db, user_id, exam_id)

@router.get("/overview")
def get_plan_overview(user_id: str = "default_user", db: Session = Depends(get_db)):
    return PlanService.get_progress_overview(db, user_id)
