FROM python:3.10.4
WORKDIR /app
COPY . /app
RUN pip3 install -r requeriments.txt
CMD ["python3", "backend/app.py"]
