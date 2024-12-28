FROM docker.io/python:3.12.2-slim-bookwrom AS python

# Stage 1: Buiild our dependency wheels
FROM python AS python-build-stage

ARG BUILD_ENVIRONMENT=local

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev

COPY ./requirements .

RUN pip wheel --wheel-dir /usr/src/app/wheels \
    -r ${BUILD_ENVIRONMENT}.txt

# Stage 2: Run Stage
FROM python AS python-run-stage

ARG BUILD_ENVIRONMENT=local

ARG APP_HOME=/app

# pyc 파일을 가져오지 못하게해서 디스크 용량을 줄임
ENV PYTHONDONTWRITEBYTHECODE=1 \
    PYTHONUMBUFFERED=1 \
    BUILD_ENV=${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# 불필요한 패키지 자동 제거
RUN apt-get update && apt-get install --no-install-recommends -y \
    sudo git bash-completion nano ssh \
    libpq-dev gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# static 파일 폴더 생성
# django 에게 775 읽기 쓰기 실행 권한, 사용자에게 읽기 및 실행 권한
RUN addgroup --system django && \
    adduser --system --ingroup django django && \
    mkdir -p ${APP_HOME}/staticfiles && \
    chown django:django ${APP_HOME}/staticfiles && \
    chmod 775 ${APP_HOME}/staticfiles

COPY --from=python-build-stage /usr/src/app/wheels /wheels/

# pip python 패키지 관리자 캐시 비활성화
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

COPY --chown=django:django ./docker/local/django/entrypoint.sh /entrypoint.sh
COPY --chown=django:django ./docker/local/django/start.sh /start.sh

# 사용자 권한으로 실행
RUN sed - i 's\/r$//g' /entrypoint.sh /start.sh $$ \
    chmod +x /entrypoint.sh /start.sh

COPY --chown=django:django . ${APP_HOME}

USER django

ENTRYPOINT [ "/entrypoint.sh" ]
