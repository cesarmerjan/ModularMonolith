FROM python:3.11 as base

ENV PROJECT_DIRECTORY="/srv/"
WORKDIR ${PROJECT_DIRECTORY}

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

ENV \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off 


# Install pipenv and compilation dependencies
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc


# Security
ARG USER="app"
ARG GROUP="app"
RUN addgroup --system ${USER} --gid 1000
RUN adduser --system ${GROUP} \
    --ingroup ${GROUP} \
    --shell /usr/sbin/nologin \
    --uid 1000 \
    --home ${PROJECT_DIRECTORY}


FROM base as staging

RUN pipenv install --dev --system --deploy --ignore-pipfile
COPY . .

FROM base as production

RUN pipenv install --system --deploy --ignore-pipfile
COPY . .

