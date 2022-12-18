FROM python:3.9-buster as builder
ENV PYTHONUNBUFFERED=1
COPY /docker/requirements.txt /
RUN /usr/local/bin/python -m pip install --upgrade pip \
  && pip install -r requirements.txt --no-cache-dir

FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages/
RUN adduser myuser && chown -R myuser home/myuser
USER myuser
WORKDIR /home/myuser/app
CMD ["python", "server.py"]