from flask import Flask, request, jsonify
from plot_graph import plot

app = Flask(__name__)

@app.route('/plotter', methods=['POST'])
def plotter():
    if request.method == 'POST':
        data = request.files.form('data')
        if data is None:
            return jsonify({'error':'no data'})

    try:
        plot(data)

    except:
        return jsonify({'error':'error during plotting'})