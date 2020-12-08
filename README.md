# flask-plotter

Run this command in the working directory before starting:
```
$ . venv/bin/activate
```

When hosting locally, change the background image directory in plor_graph.py from `static/gestation.png` to `src/static/gestation.png`.

To host the flask app locally, using (for MacOS):
```
$ export FLASK_APP=src/main.py
$ export FLASK_ENV=development #when debugging
$ flask run
```
