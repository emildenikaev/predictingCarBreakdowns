from fastapi import Query, APIRouter
from sqlalchemy import distinct

from app.database import session
from app.models import BookingClass
from app.utils import get_fly_directions, get_fly_numbers_by_direction

router = APIRouter(prefix='/api/v1/filters', tags=['filters'])


@router.get("/directions/")
async def get_directions():
    """Направления рейсов."""
    try:
        flight_directions = get_fly_directions()

        return {'status': 200, 'directions': flight_directions}
    except Exception as e:
        return {'status': 500, 'error': str(e)}


@router.get("/flight_numbers/")
async def get_flight_numbers(
        direction: str = Query(..., description='Направление рейс', example="Москва - Сочи"),
):
    """
    Номера рейсов по направлению
    """

    try:
        standard_directions = get_fly_numbers_by_direction()
        flights = standard_directions.get(direction, None)

        return {'status': 200, 'flight_numbers': flights}

    except Exception as e:
        return {'status': 500, 'error': str(e)}


@router.get("/booking_classes/")
async def get_booking_classes():
    """Классы бронирования"""
    query = session.query(distinct(BookingClass.SEG_CLASS_CODE)).all()
    classes = [row[0] for row in query]

    return {"status": 200, "booking_classes": sorted(classes)}


@router.get('/scenarios/')
async def get_scenarios():
    """Сценарный прогноз"""
    return {
        'status': 200,
        "scenarios": ['позитивный (+20%)', 'нейтральный (+5%)', 'негативный -(20%)', 'реальный 2020 год']
    }


@router.get('/cabins/')
async def get_cabins():
    """Фильтр кабины, необязательный."""
    query = session.query(distinct(BookingClass.SSCL1)).all()
    classes = [row[0] for row in query]

    return {"status": 200, "cabin_classes": sorted(classes)}
