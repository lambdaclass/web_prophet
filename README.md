# Web Prophet

Web Prophet is a small tool that aims to help to analyze time series data using [Prophet](https://facebook.github.io/prophet/) in a simple way, without any coding experience.

## Getting Started

### Prerequisites

First of all you'll need a working Python 3 environment.
This project is developed using [pyenv](https://github.com/pyenv/pyenv) as version manager.

### Installing

To install the required packages run:

```
$ make install
```

### Running the project

Run the following command to start the server:
```
$ make run
```

## Usage

After starting the server, open your browser and go to `http://localhost:5000` to see the upload form.
Then choose a CSV file of your preference and submit the form. Wait a few seconds and enjoy the generated plots.

## Built With

* [Python 3.7](https://www.python.org/downloads/release/python-370/)
* [Flask](http://www.dropwizard.io/1.0.2/docs/) 
* [Prophet](https://github.com/facebook/prophet)
* [pyenv](https://github.com/pyenv/pyenv)
