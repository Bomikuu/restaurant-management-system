FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./requirements/requirements.txt /code/
RUN pip install -r requirements.txt
CMD ./command.sh
