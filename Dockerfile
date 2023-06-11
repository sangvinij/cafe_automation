FROM python:3.11.3-slim
ARG group

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Creating a new user, upgrading pip to the latesr version and installing poetry
RUN useradd -ms /bin/bash newuser && \
    python -m pip install --upgrade pip && \
    pip install poetry

# Copy pyproject.toml and poetry.lock to install dependencies
WORKDIR /cafe
COPY pyproject.toml poetry.lock ./

# Installing dependencies to system python
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction $group

# Сopy the remaining files
COPY . .

# Runing the file as an executable script
RUN chmod +x entrypoint.sh

# Changing user 
USER newuser

# Launching the script
ENTRYPOINT [ "./entrypoint.sh" ]

# Checking health status
HEALTHCHECK --interval=3s --timeout=10s --start-period=15s --retries=5 \
  CMD curl -f http://localhost:8000/ || exit 1
