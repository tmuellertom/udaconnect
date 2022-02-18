FROM python:3.8

WORKDIR .

COPY . .
# Do upgrade becaus Building wheel for grpcio took forever
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

EXPOSE 5005

COPY . .
ENTRYPOINT ["python", "server.py"]