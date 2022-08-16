FROM python:3.9-slim-buster

LABEL maintainer="xq_work@outlook.com"

ENV PYTHONUNBUFFERED=1
ENV GROUP_ID=1000 \
    USER_ID=1000

RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt

# ENTRYPOINT [ "python" ]

# CMD ["realway/app.py" ]

# RUN poetry install

# EXPOSE 3000
# CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]
