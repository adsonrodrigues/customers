<!--
*** Thank you for viewing my README. If you have any suggestions
*** that can improve it further fork the repository and create
*** a Pull Request or open an Issue with the tag "suggestion".
*** Thank you again! Now let's run this incredible project. 
-->

<!-- PROJECT SHIELDS -->

# Customers API 
___
[![build](https://img.shields.io/badge/build-passing-green)](build) [![coverage](https://img.shields.io/badge/coverage-0%25-red)](coverage) [![docker](https://img.shields.io/badge/docker%20build-automated-important)](docker) [![docker-version](https://img.shields.io/badge/version-19.03.8-important)](docker-version) [![license](https://img.shields.io/badge/license-MIT-blue)](license)


<!-- TABLE OF CONTENTS -->

## Table of Contents
___
* [Table of Contents](#table-of-contents)
* [About the Project](#about-the-project)
  * [Done With](#done-with)
* [Starting](#starting)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Run Project](#run-project)
* [Contribution](#contribution)
* [License](#license)
* [Contact](#contact)

<!-- ABOUT THE PROJECT -->

## About the Project
___
_This a simple Django REST API which provides information about customers and integrates with the google maps API_

## Done With
___
- [Django](https://www.djangoproject.com/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [Django Rest Framework](https://www.django-rest-framework.org/) - Django REST framework is a powerful and flexible toolkit for building Web APIs.
- [Python Client for Google Maps Services](https://github.com/googlemaps/google-maps-services-python) - This library brings the Google Maps Platform Web Services to your Python application.
- [Django Environ](https://github.com/joke2k/django-environ) - Django Environ allows you to use Twelve-factor methodology to configure your Django application with environment variables.
- [Docker](https://www.docker.com/) - Docker simplifies and accelerates your workflow, while giving developers the freedom to innovate with their choice of tools, application stacks, and deployment environments for each project.
- [Docker Compose](https://docs.docker.com/compose/) - Compose is a tool for defining and running multi-container Docker applications.

<!-- GETTING STARTED -->

## Starting
___
To be able to use the project follow the steps below.

### Prerequisites
___
###### docker

- [Official docs](https://docs.docker.com/get-docker/)
- [How to install in Fedora](https://docs.docker.com/engine/install/fedora/)
- [How to install in MacOS](https://docs.docker.com/docker-for-mac/install/)
- [How to install in Windows](https://docs.docker.com/docker-for-windows/install/)

###### docker compose

- [How to install docker compose](https://docs.docker.com/compose/install/)

### Installation
___
```sh
$ docker-compose up -d --build # (only first)
$ docker-compose exec service python3 manage.py migrate # (only first)
$ docker-compose exec service python3 manage.py createsuperuser # (only first)
```

### Run project
___
```sh
$ docker-compose up -d 
$ docker-compose exec service bash
$ python manage.py runserver 0.0.0.0:8000
```

<!-- CONTRIBUTING -->

## Contribution 
_Contributions are what make the open source community an incredible place to learn, inspire and create. Any contribution you make will be **much appreciated**._

1. Fork the project
2. Create a Branch for your Feature (`git checkout -b feature/name_branch`)
3. Add your changes (`git add file`)
4. Commit your changes (`git commit -m 'Adding an awesome Feature!`)
5. Push the Branch (`git push origin feature/name_branch`)
6. Open a Pull Request

<!-- LICENSE -->

## License
___
The MIT License (MIT)

Copyright (c) [2020] [Adson Rodrigues](https://github.com/adsonrodrigues)

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

<!-- CONTACT -->

## Contact
___

Adson Rodrigues - [Linkedin](https://www.linkedin.com/in/adsonr/)