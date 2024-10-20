# Python Developer Challenge

The challenge is: "Create a Backend file processor project"

This project involves the development of a backend application in Python that allows for the upload and validation of flat files (.txt or .csv) through an interface. The application processes the data, inserts the records into a database using an ORM (Object-Relational Mapping), and enables querying each record by its ID.

## Pre requisites

- Docker installed on your machine ([Install Docker](https://docs.docker.com/get-docker/))


## Environment Variables

Add and set .env in project root with the vars:


#### Set Database credentials
- `POSTGRES_PORT`= 5432
- `POSTGRES_HOST`:= db
- `POSTGRES_DB`= postgres
- `POSTGRES_USER`= postgres
- `POSTGRES_PASSWORD`= postgres


#### Set for postgresql database docker image
- `POSTGRES_DB="{DB_NAME}"`
- `POSTGRES_USER="{DB_USER}"`
- `POSTGRES_PASSWORD="{DB_PASSWORD}"`


#### Set postgresql database uri
- `DATABASE_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}?sslmode=disable"`


#### Set docker image name
- `IMAGE_NAME=file_processor`


## Building the Docker containers

Follow the next steps to build the python and db containers:

1. Open a terminal.
2. Navigate to the directory of the project.
3. Run the following command:

    ```bash
    docker compose build --no-cache
    docker compose up -d 
    ```

    You can remove flag `-d` to show in terminal logs while container is running.

    Or instead of, you can try:
    ```bash
    make build
    make up
    ```

Now you can consume the api on your localhost: http://localhost:80 or use it in via swagger http://localhost/docs


# How to use 
TODO

### GET method
TODO

### POST method
TODO