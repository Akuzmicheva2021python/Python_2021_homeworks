# docker build . -t cbrinfo
# docker run -p 8080:8000 cbrinfo

FROM python:3.9

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system

EXPOSE 8000

COPY ./weather /weather

WORKDIR /weather

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]