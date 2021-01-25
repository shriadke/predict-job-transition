FROM python:3.7.9

# Set the working directory to /app
WORKDIR /opt/app

RUN apt-get update && apt-get clean

COPY ./ .

RUN pip3 install -r requirements.txt

EXPOSE 9000
ENTRYPOINT ["python3", "app.py"]