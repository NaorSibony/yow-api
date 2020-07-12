FROM python:3-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app /yow_api/app
COPY manage.py /yow_api
WORKDIR /yow_api
ENTRYPOINT python /yow_api/manage.py run