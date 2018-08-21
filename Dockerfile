# Using lightweight apline image
FROM python:3.6-apline

#installing packages
RUN apk update
RUN pip install --no-cache-dir pipenv

# Definining working directory and adding source code
WORKDIR /usr/src/app
COPY Pipfile pipfile.lock bootstrap.sh ./
COPY cashman ./cashman

#Install API dependencoes
RUN pipenv install


# Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]