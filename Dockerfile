FROM python:latest
WORKDIR /usr/src/app
COPY ./app.py /usr/src/app/app.py
COPY ./requirements.txt /usr/src/app/requirements.txt
COPY ./feedparse.py /usr/src/app/feedparse.py
COPY ./rssitem.py /usr/src/app/rssitem.py
COPY ./static/ /usr/src/app/static/
COPY ./templates/ /usr/src/app/templates/
EXPOSE 5000
RUN pip install -r /usr/src/app/requirements.txt
ENV LISTEN_PORT=5000
CMD [ "python3", "/usr/src/app/app.py" ]