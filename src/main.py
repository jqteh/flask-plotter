from flask import Flask, request, jsonify, send_file
from plot_graph import plot

app = Flask(__name__, static_url_path='/bin')

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
        except:
            return jsonify(message)

        pathname = 'bin/figure.png'
        return send_file(pathname, mimetype='image/png')