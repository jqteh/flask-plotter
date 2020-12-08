from flask import Flask, request, jsonify, send_file
from plot_graph import plot
import io

app = Flask(__name__, static_url_path='/bin')

@app.route('/plotter', methods=['POST'])
def plotter():
    if request.method == 'POST':
        if not request.is_json      # check if the incoming data is JSON
            return jsonify({'ERROR': 'The posted data is not JSON'})

        data = request.get_json()
        #print(data)

        if data is None:
            return jsonify({'ERROR':'No data contained in JSON'})

        try:
            img = plot(data)    # the plot function returns the url of the image created if the plot is successful, otherwise it returns error message
            img.seek(0)     # move the pointer of the file to the start
        except:
            return jsonify(img)

        return send_file(img, mimetype='image/png')     # mimetype should be specified correctly