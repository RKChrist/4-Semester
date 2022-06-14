FROM python:3.10


# dont write pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# dont buffer to stdout/stderr
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
ADD . /app

WORKDIR /app
# # Update packages
RUN apt-get update
# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt


# Run the application
CMD ["uvicorn","app.app:app", "--host","0.0.0.0", "--port", "80"]