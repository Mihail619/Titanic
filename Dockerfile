FROM python:3.9.13

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY Requirements.txt .

 
RUN pip install -r Requirements.txt

COPY . .

CMD gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

    