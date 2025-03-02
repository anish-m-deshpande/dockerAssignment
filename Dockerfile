# Use a minimal Python base image
FROM python:3.9.18-alpine3.18

# Setting the working directory
WORKDIR /home

# Installing necessary dependencies (temporary build tools removed after use)
RUN apk add --no-cache --virtual .build-deps \
    gcc musl-dev libffi-dev && \
    pip install --no-cache-dir ipython && \
    apk del .build-deps && \
    rm -rf /var/cache/apk/*

# Copying only necessary files
COPY scripts.py /home/scripts.py
COPY data /home/data

# Running the script on container start
CMD ["python", "/home/scripts.py"]

