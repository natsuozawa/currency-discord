FROM python:3.9

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get upgrade -y

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

COPY index.py .

ENTRYPOINT [ "python", "index.py" ]
