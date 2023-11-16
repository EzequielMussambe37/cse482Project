# Author: Jake Yax
# `docker exec -it cse482-container_flask-app bask`

# Instantiate Ubuntu 20.04
FROM ubuntu:20.04
LABEL maintainer="Jake Yax"
LABEL description="Docker Image for CSE 482 Steam Recommendation Model"

# Update Ubuntu Software Repo
RUN apt update
RUN apt-get update -qq

# Install MySQL and create the database
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get install -y mysql-server
RUN service mysql start && mysql -e "CREATE USER 'master'@'localhost' IDENTIFIED BY 'master';CREATE DATABASE db; GRANT ALL PRIVILEGES ON db.* TO 'master'@'localhost';"

# Add the Flask application and install requirements
RUN apt -y install python3-pip
RUN apt -y install vim
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
ENV PORT 8080
ENV FLASK_ENV=production
CMD service mysql start && exec gunicorn --bind :$PORT --workers 1 --thread 8 --timeout 0 app:app