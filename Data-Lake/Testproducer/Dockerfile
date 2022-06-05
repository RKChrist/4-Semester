FROM python:3.10


# dont write pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# dont buffer to stdout/stderr
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
ADD . /app

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade --no-cache-dir pip && pip install -r requirements.txt

# Copy the source from the current directory to the Working Directory inside the container
COPY . .

# Run the application
CMD ["python", "test.py"]