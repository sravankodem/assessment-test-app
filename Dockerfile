FROM python:3.6
WORKDIR /app
COPY . /app
EXPOSE 8080
CMD ["python","app.py"]


