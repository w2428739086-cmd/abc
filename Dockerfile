FROM python:3.12-slim
WORKDIR /app
COPY captcha.py .
EXPOSE 8080
CMD ["python3", "captcha.py"]
