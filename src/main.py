from flask import Flask, request, jsonify
from plot_graph import plot

app = Flask(__name__)

@app.route('/plotter', methods=['POST'])
def plotter():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({'error': 'The posted data is not JSON'})

        data = request.get_json()
        print(data)
        
        if data is None:
            return jsonify({'error':'no data'})

        try:
            message = plot(data)
            return jsonify({'message': message})
        except:
            return jsonify({'error':'error during calling plot function'})