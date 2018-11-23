# Postgis dockerfile
FROM mdillon/postgis

RUN apt-get update \
      && apt-get install -y --no-install-recommends \
	   p7zip-full \
      && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pgdump pgdumxp


