FROM  python:3.11-slim-bullseye

ENV PURE_PYTHON 1

RUN apt-get update \
    && apt-get -yq --no-install-recommends install \
    build-essential libpq5 libpq-dev git iproute2 procps netcat \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip

RUN pip install poetry==1.6.1 \
    && poetry config virtualenvs.create false

RUN pip install git+https://github.com/tmikus/pycld2.git


WORKDIR /code

ARG BUILD_DATE="NA"
ARG VCS_REF="NA"

COPY  gunicorn.py.ini /code/

COPY pyproject.toml poetry.lock /code/
RUN poetry install --no-root --no-interaction --no-ansi

ENV PYTHONPATH="${PYTHONPATH}:/code/"

ENV _PIP_USE_IMPORTLIB_METADATA=0