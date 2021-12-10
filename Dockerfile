FROM python:3.8.5 
ENV PYTHONUNBUFFERED 1 
# RUN apt-get install \
#   libpq-dev \
#   && apt-get clean
RUN mkdir /app 
WORKDIR /app 
COPY requirements.txt /app/ 
RUN pip install -r requirements.txt
COPY . /app/