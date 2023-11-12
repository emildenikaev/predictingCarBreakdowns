from typing import Optional
from fastapi import Query, APIRouter
from fastapi.responses import FileResponse
from fastapi import File, UploadFile
from os import getcwd
import os
import shutil

from fastapi.exceptions import HTTPException
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

# ------------------------------------------------------------------------------------------


@router.get('/download/{name_file}', name='user:file_of_recomendation')
async def get_file_rec(name_file: str):
    return FileResponse(path=getcwd() + "/" + name_file, media_type='application/octet-stream', filename=name_file)

# ------------------------------------------------------------------------------------------


@router.post("/uploadfile/{name_file}", name='user:file')
async def create_upload_file(file: UploadFile = File(...)):
    # Get the file size (in bytes)
    file.file.seek(0, 2)
    file_size = file.file.tell()

    # move the cursor back to the beginning
    await file.seek(0)

    if file_size > 2 * 1024 * 1024 * 200:
        # more than 400 MB
        raise HTTPException(status_code=400, detail="File too large")

    # check the content type (MIME type)
    content_type = file.content_type
    print(content_type)
    if content_type not in ["text/csv"]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    # save file
    upload_dir = os.path.join(os.getcwd(), "data_for_pred")
    print(upload_dir)
    print(os.getcwd())
    # Create the upload directory if it doesn't exist
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # get the destination path
    dest = os.path.join(upload_dir, file.filename)
    print(dest)

    # copy the file contents
    with open(dest, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}
