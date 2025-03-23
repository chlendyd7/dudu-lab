# alpine 사용 경량화, 초기 설정 중 이므로 사용
FROM python:3.11-alpine

RUN apk add --no-cache gcc python3-dev musl-dev linux-headers

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/lab

EXPOSE 8000
# CMD ["gunicorn", "conf.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
# CMD ["gunicorn", "-k", "gevent", "--bind", "0.0.0.0:8000", "conf.wsgi:application"]

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
