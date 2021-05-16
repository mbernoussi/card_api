ARG BASE_IMAGE
ARG BASE_IMAGE_TAG
FROM ${BASE_IMAGE}:${BASE_IMAGE_TAG} as builder

ARG USERNAME
ARG APP_DIR

RUN adduser -D ${USERNAME}

RUN apk add build-base

RUN mkdir -p ~/${API_DIR}

WORKDIR /home/${USERNAME}/${APP_DIR}

COPY requirements.txt requirements.txt

COPY card_api card_api

COPY .flaskenv .

COPY entrypoint.sh .

RUN python -m venv venv && \
    venv/bin/pip install --upgrade pip && \
    venv/bin/pip install -r requirements.txt

FROM python:3.7.9-alpine

ARG USERNAME
ARG APP_DIR

RUN adduser -D ${USERNAME}

COPY --from=builder --chown=${USERNAME}:${USERNAME} /home/${USERNAME} /home/${USERNAME}

USER ${USERNAME}
WORKDIR /home/${USERNAME}/${APP_DIR}

#ENTRYPOINT ["sleep"]

#CMD ["1000000"]

ENTRYPOINT ["./entrypoint.sh"]