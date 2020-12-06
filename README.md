# flask-plotter

Run this command in the working directory before starting:
```
$ . venv/bin/activate
```

Before running or testing, make sure that the url and the directories in the main.py and plot_graph.py are configured correctly

To host the flask app locally, using (for MacOS):
```
$ export FLASK_APP=src/main.py
$ flask run
```

The flask app might not work if the directory `\src\bin` does not exsit. If that's the case, create an empty folder.