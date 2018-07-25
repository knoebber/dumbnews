# Dumb News Aggregator
This project provides a simple news aggregator built as a web app to be run on a personal server. Simply fill a configuration file with the feeds you wish to track in the `dumbnews/feeds` directory, and navigate to the feeds you wish to see.

## Server Setup
(Note that this guide assumes you are using a Linux server, and are not planning to develop this application beyond creating custom feeds)

This project is built using Python3 and the Flask web framework. First, make sure you have Python3 installed on your server. Then, install the required packages listed in the `requirements.txt` file using pip:

```
$ pip install -r requirements.txt
```

Once you have successfully installed the necessary dependencies, you need to show direct flask to the appropriate directory containing the app:

```
$ export FLASK_APP=dumbnews
```

Then, to run the application simply use the `flask run` command:

```
$ flask run --host=0.0.0.0
```

## Development Setup
If you would like to work on the project, or test it on your local machine, it's recommended that you set up a virtual enviroment using `virtualenv`, which is included with Python3 installations. To set up your virtual environment, navigate to the outermost directory of the project, then initialize and activate your virtual environment with the following commands:

```
$ python3 -m venv venv
$ . venv/bin/activate
```

Once your virtual environment is activated, you can install the necessary dependencies:

```
$ pip install -r requirements.txt
```

Then, configure the app and enable debug mode for lazy-loading:

```
$ export FLASK_APP=dumbnews
$ export FLASK_DEBUG=1
```

When you wish to see the app, use `flask run` as in the setup documentation, without the `--host` specification so that you do not allow other computers on the network to connect:

```
$ flask run
```

Finally, navigate your web browser to "localhost:5000" to interact with the application.

## Feed Configuration
Feed parsing is handled with the `feedparser` library, and therefore handles all of their [supported feed formats](https://pythonhosted.org/feedparser/introduction.html).

All configuration files must be placed into the 'dumbnews/feeds' directory. The app sorts and displays configurations by their associated file name, so if you wish to have a configuration labeled "World News" within the app, name your associated configuration file "World\ News". Configuration files should have a list of newline-separated urls associated with feeds you wish to be displayed together.
