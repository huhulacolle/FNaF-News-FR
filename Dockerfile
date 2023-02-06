FROM python:3.11.1-slim
WORKDIR /bot
COPY . .
RUN pip install -r requirements.txt
CMD [ "python", 'main.py' ]