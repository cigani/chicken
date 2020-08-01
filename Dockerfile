FROM python:3.8
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Adds our application code to the image
COPY . code
WORKDIR code

EXPOSE 8000

COPY ./entrypoint_dev.sh .
RUN ["chmod", "+x", "/code/entrypoint_dev.sh"]


RUN ["chmod", "+x", "app/dataseed.py"]
# Run the production server
CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - chicken.wsgi:application
ENTRYPOINT ["/code/entrypoint_dev.sh"]


