# Web Prophet

Web Prophet is a small tool that aims to help to analyze time series data using [Prophet](https://facebook.github.io/prophet/) in a simple way, without any coding experience.

## Getting Started

### Prerequisites

First of all you'll need a working Python 3 environment with [pipenv](https://pipenv.readthedocs.io/en/latest/) installed.

### Installing

To create a virtualenv and install the required packages run:

```
$ make deps
```

### Running the project

Run the following command to start the server:
```
$ make start
```

## Usage

After starting the server, open your browser and go to `http://localhost:5000` to see the upload form.
Then choose a CSV file of your preference and submit the form. Wait a few seconds and enjoy the generated plots.


## Built With

* [Python 3.7](https://www.python.org/downloads/release/python-370/)
* [Flask](http://flask.pocoo.org/)
* [Prophet](https://github.com/facebook/prophet)
* [pypenv](https://pipenv.readthedocs.io/en/latest/)
