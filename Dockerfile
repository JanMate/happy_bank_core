FROM python:3.9

LABEL description="A simple bank core app for mentoring purposes" \
      author="Oleksandr6676" \
      contributor="JanMate" \
      app="happy-bank-core" \
      version=1.0.0

ENV PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    POETRY_VERSION=1.1.2 \
    USER_NAME=core

# Create system user with less privileges than root
RUN addgroup --gid 123 "${USER_NAME}" \
    && adduser --system --uid 1001 --group "${USER_NAME}" \
    && mkdir /data \
    && chown -R "${USER_NAME}":"${USER_NAME}" /data

WORKDIR /app

# Add source code
COPY pyproject.toml poetry.lock ./
COPY happy_bank_core core

# Set ownership of the core folder
RUN chown -R "${USER_NAME}":"${USER_NAME}" ./core

USER "${USER_NAME}"

# Update path env var with path to user's binaries
ENV PATH="${PATH}:/home/${USER_NAME}/.local/bin"

# Install poetry
RUN pip install --no-cache-dir --upgrade pip \
    && curl -sSL "https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py" | python -

# Setup app deps
RUN poetry install --no-dev --no-interaction --no-ansi

# Run flask app via poetry in generated venv
ENTRYPOINT ["poetry", "run"]
CMD ["python3", "core/app.py"]
