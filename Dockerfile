FROM sleekybadger/libpostal:1.1-alpha-alpine as libpostal-build

FROM python:3.7.1-alpine

COPY --from=libpostal-build /data /data
COPY --from=libpostal-build /usr/lib/libpostal.so /usr/lib/libpostal.so
COPY --from=libpostal-build /usr/lib/libpostal.so.1 /usr/lib/libpostal.so.1
COPY --from=libpostal-build /usr/include/libpostal /usr/include/libpostal

ARG WORKERS=2
ARG PORT=8001
ENV WORKERS ${WORKERS}
ENV PORT ${PORT}

RUN apk add --no-cache build-base

RUN mkdir /app
WORKDIR /app

COPY app.py .

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE ${PORT}

CMD python -m sanic app.app --host=0.0.0.0 --port=$PORT --workers=$WORKERS
