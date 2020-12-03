from flask import Flask, request, jsonify
from plot_graph import plot

app = Flask(__name__)

@app.route('/plotter', methods=['POST'])
def plotter():
    if request.method == 'POST':
        data = request.json
        print(data)
        if data is None:
            return jsonify({'error':'no data'})

        try:
            plot(data)
            return jsonify({'correct':'success'})
        except:
            return jsonify({'error':'error during plotting'})