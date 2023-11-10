from typing import Optional
from fastapi import Query, APIRouter
# from app.models import model
from app.models import (
    model_predict,
)

router = APIRouter(prefix='/api/v1/calculation', tags=['calculation'])

@router.get("/predict")
async def get_predictions(
        number_1: int = Query(..., description="Номер", example="1120"),
        date: str = Query(..., description="Дата", example="2018-05-29"),
        class_1: str = Query(..., description="Класс", example="Y"),
        period: Optional[int] = Query(1, ge=1, le=12, description="Период(в месяцах)", example='1')
):
    """
    Получение предсказаний моделью
    """
    try:
        predictions = model_predict(number_1, date, class_1, period)
        print('Ok')

        return {'status': 200, "data": predictions}

    except Exception as e:
        return {'status': 500, "error": str(e)}
