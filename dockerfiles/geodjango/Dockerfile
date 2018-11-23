# Django dockerfile
FROM python:3.6

RUN apt-get update -y && \
    apt-get install -y \
      binutils \
      libproj-dev \
      gdal-bin \
      python-gdal \
      locales && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY tpfinal tpfinal
COPY requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["python", "tpfinal/manage.py", "runserver", "0.0.0.0:8001"]
