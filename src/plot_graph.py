import matplotlib.pyplot as plt
import numpy as np
import io

def plot(data_in_json):

    try:
        # parse the JSON data
        x = np.array(data_in_json["time"])
        y = np.array(data_in_json["measurements"])
    except:
        return {'ERROR': 'Unmatching JSON keys'}

    try:
        back = plt.imread("static/gestation.png")
        fig, ax = plt.subplots()
        plt.scatter(x, y, s=100 , c='r', marker='x', linewidths=1)
        ax.imshow(back, extent=[23, 42, 17, 39])
    except Exception as e:
        print(e)
        return {'ERROR': 'Problem arised during plotting'}

    try:
        img = io.BytesIO()      # img is the url for the memory in buffer
    except:
        return {'ERROR': 'Problem arised during io'}

    try:
        fig.savefig(img, bbox_inches='tight', format='png', dpi=400)        # save the image into the url of the memory created just now
        plt.close(fig)
        return img
    except:
        return {'ERROR': 'Problem arised saving or reurning'}

