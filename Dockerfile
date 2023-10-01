# VERSION 1
## Use the official Python base image
#FROM python:3-alpine3.16
#
## Set the working directory
#WORKDIR /web/tcb_api
#
## Set environment variables
#ENV PYTHONUNBUFFERED 1
#ENV PYTHONFAULTHANDLER 1
#
## Create a directory and copy the project into it
#RUN mkdir -p /web
#COPY . /web
#
## Install dependencies
#RUN pip install --upgrade pip
#RUN pip install gunicorn
#RUN python -m pip install --upgrade pip
#COPY requirements.txt /web
#RUN pip install -r /web/requirements.txt
#
## Install SQLite and its development libraries
#RUN apk add --no-cache sqlite sqlite-dev
#
## Expose port 8000
#EXPOSE 8000
#
## Define the command to run when the container starts
##CMD ["sh", "-c", "python /web/tcb_api/manage.py migrate && python /web/tcb_api/manage.py runserver 0.0.0.0:8000"]
#CMD ["python", "./web/manage.py", "migrate"]
#CMD ["python", "./web/manage.py", "runserver", "0.0.0.0:8000"]

# VERSION 2
# Use the official Python base image
FROM python:3-alpine3.16

# Install build essentials and development libraries.
# Added the installation of build-base, libffi-dev, and openssl-dev packages using apk. These packages provide essential
# build tools and libraries for compiling C code and building Python packages that depend on C extensions.
RUN apk add --no-cache build-base libffi-dev openssl-dev

# Set work directory
WORKDIR /web/tcb_api

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONFAULTHANDLER 1

# Create directory and copy project
RUN mkdir -p /web
COPY . /web

# Install dependencies
RUN pip install --upgrade pip
RUN pip install gunicorn
COPY requirements.txt /web
RUN pip install -r /web/requirements.txt

# # Continue with the rest of your Dockerfile
# CMD ["python", "./web/manage.py", "migrate"]
# CMD ["python", "./web/manage.py", "runserver", "0.0.0.0:8000"]
RUN python /web/manage.py migrate
RUN python /web/manage.py runserver 0.0.0.0:8000
