FROM python:bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .s

EXPOSE 8000

# Run the Django app when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]