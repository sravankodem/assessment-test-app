FROM python:3.6

COPY ./requirements.txt /app/requirements.txt
WORKINGDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]


