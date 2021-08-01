# text-summarizer

[![Continuous Integration and Delivery](https://github.com/rodrigodelmonte/text-summarizer/actions/workflows/main.yml/badge.svg)](https://github.com/rodrigodelmonte/text-summarizer/actions/workflows/main.yml)
[![Code Style Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

## Overview

Text summarizer is an personal project to practice learns from the course [Test-Driven Development with FastAPI and Docker](https://testdriven.io/courses/tdd-fastapi/). The project is a CRUD API to summarize blog posts powered by libraries like FastAPI, tortoise-orm, and Newspaper3k.

The project is deployed on Heroku [here](https://mighty-garden-15987.herokuapp.com/docs).

### Endpoints

|  Endpoint |  HTTP Method |  CRUD Method |  Result |
|---|---|---|---|
|  /summaries |  GET |  READ |  get all summaries |
|  /summaries/:id| GET |  READ | get a single summary  |
|  /summaries| POST  |  CREATE |  get a single summary |
|  /summaries/:id| PUT  |  UPDATE |  update a summary |
|  /summaries/:id| DELETE  |  DELETE |  delete a summary

## Demo
[![asciicast](https://asciinema.org/a/hEy3RKySIpHnWTxhB2lre3vkY.svg)](https://asciinema.org/a/hEy3RKySIpHnWTxhB2lre3vkY)

## Development

To have a development environment this project requires [Docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/). Please review the files [Makefile](Makefile) and [docker-compose.yml](docker-compose.yml)  for more details:

```sh
make build # Build docker image
make run # Runs docker image
make create-db # Create required table schemas
make test # Runs tests
```

## Contribute

- Fork the repo (<https://github.com/rodrigodelmonte/text-summarizer/fork>)
- Create your feature branch (`git checkout -b feature/fooBar`)
- Commit your changes (`git commit -am 'Add some fooBar'`)
- Push to the branch (`git push origin feature/fooBar`)
- Create a new Pull Request
