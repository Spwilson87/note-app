FROM python:3

WORKDIR /usr/notes

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py" ]