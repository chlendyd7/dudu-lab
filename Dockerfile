# alpine 사용 경량화, 초기 설정 중 이므로 사용
FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/lab

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
