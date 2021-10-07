FROM python:3.10-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=pil_flask

EXPOSE 5000
CMD [ "python", "pil_flask.py" ]