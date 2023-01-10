FROM python:3.8

ENV LC_ALL C.UTF-8

WORKDIR /app

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

COPY . .

EXPOSE 8080

#RUN python manage.py migrate
CMD ["python", "manage.py", "migrate"]
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8080"]