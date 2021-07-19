# DRO-Health-API

API Service backing client interfaces

## Technologies

* [Python 3.9](https://python.org) : Base programming language for development
* [SQLite](https://www.sqlite.org/index.html) : Application relational databases for development, staging and production environments
* [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
* [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
* [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) : Continuous Integration and Deployment
* [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration

## Description
There are two main endpoints for this api,
- The first endpoint `http://127.0.0.1:8000/womens-health/api/create-cycles`, this endpoint takes a POST request with the following expected values
```
{
  “Last_period_date”:”2020-06-20”
  “Cycle_average”:25
  “Period_average”:5
  “Start_date”:”2020-07-25”,
  “end_date”:”2021-07-25”
}
```
the endpoint calculates the amount of menstral cycles expected based on the time range given combined with cycle_average and period_average.
Expected response
```
{
    "total_created_cycles": 12
}
```

- The second endpoint `http://127.0.0.1:8000/womens-health/api/cycle-event/?date=2021-08-14`, this endpoint takes a query parameter `date` which is equal to a particular date of which is expected to return an event occuring on the particular date given based on the parameters given for the first endpoint.

Expected response
```
[
    {
        "event": "mentral cycle starts",
        "date": "2021-08-14"
    }
]
```
## Getting Started

Getting started with this project is very simple, all you need is to have Git and Docker Engine installed on your machine. Then open up your terminal and run this command `git clone https://github.com/funsojoba/DRO-Health-API.git` to clone the project repository.

Change directory into the project folder `cd dro-health-api` and build the base python image used for the project that was specified in ***dockerfile*** by running ` docker build . ` *Note the dot (.) at end of the command*.

Spin up other services needed for the project that are specified in ***docker-compose.yml*** file by running the command `docker-compose up`. At this moment, your project should be up and running with a warning that *you have unapplied migrations*.

Open up another terminal and run this command `python manage.py makemigrations` for creating new migrations based on the models defined and also run `python manage.py migrate` to apply migrations.

In summary, these are the lists of commands to run in listed order, to start up the project.

```docker
1. git clone https://github.com/funsojoba/DRO-Health-API.git
2. cd dro-health-api
3. docker build .
4. docker-compose up
5. python manage.py makemigrations
6. python manage.py migrate
7. user ctrl+c to quit server
```

## Running Tests

Currently, truthy tests has been provided in each of the application defined in the project, before running the tests with the following command make sure that your api service is up and running.

Run 
```
docker-compose exec api python manage.py test DRO_project
```

## License

The MIT License 
