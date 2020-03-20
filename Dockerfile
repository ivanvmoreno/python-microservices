FROM python:buster

RUN pip install pipenv

COPY Pipfile* /tmp/

RUN cd /tmp && pipenv lock --requirements > requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY app/ /tmp/app/

WORKDIR /tmp

CMD python -m app.services.run