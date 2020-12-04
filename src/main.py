from flask import Flask, request, jsonify
from plot_graph import plot

app = Flask(__name__)

@app.route('/plotter', methods=['POST'])
def plotter():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({'ERROR': 'The posted data is not JSON'})

        data = request.get_json()
        print(data)

        if data is None:
            return jsonify({'ERROR':'No data contained in JSON'})

        try:
            message = plot(data)
            return jsonify(message)
        except:
            return jsonify({'ERROR':'Error arised when plot function is called'})