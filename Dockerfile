
FROM python:latest

COPY . /var/www
WORKDIR /var/www
ENV PORT=8000
EXPOSE $PORT
RUN pip install poetry && poetry config virtualenvs.create false && poetry install
ENTRYPOINT python -m django run --host=0.0.0.0 --port=$PORT --reload