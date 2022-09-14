FROM python:3.7-alpine
COPY . issues
RUN apk --update add gcc build-base freetype-dev libpng-dev openblas-dev libffi-dev
RUN python -m pip install --upgrade pip && pip install -r issues/requirements.txt
