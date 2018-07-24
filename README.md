#Dumb News Aggregator
This project provides a simple news aggregator built as a web app to be run on a personal server. Simply fill a configuration file with the feeds you wish to track in the 'dumbnews/feeds' directory, and navigate to the feeds you wish to see.

##Setup
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

##Feed Configuration
Feed parsing is handled with the `feedparser` library, and therefore handles all of their [supported feed formats](https://pythonhosted.org/feedparser/introduction.html).

All configuration files must be placed into the 'dumbnews/feeds' directory. The app sorts and displays configurations by their associated file name, so if you wish to have a configuration labeled "World News" within the app, name your associated configuration file "World\ News". Configuration files should have a list of newline-separated urls associated with feeds you wish to be displayed together.

An example configuration file can be found at `feeds/Example`.
