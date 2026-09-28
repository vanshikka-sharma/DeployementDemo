FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "DeploymentDemo.wsgi:application", "--bind", "0.0.0.0:8000"]