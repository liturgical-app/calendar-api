FROM python:3.12-alpine
WORKDIR /code
COPY src/app/requirements.txt /code
RUN pip3 install -r requirements.txt --no-cache-dir
COPY .. /code
EXPOSE 3000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:3000", "-k", "gevent", "-w", "1", "src.app.app:app"]