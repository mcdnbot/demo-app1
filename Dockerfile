FROM python:3.6-alpine
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY ./templates /app/templates
COPY app.py /app
WORKDIR /app
EXPOSE 8080
CMD ["python", "app.py"]
