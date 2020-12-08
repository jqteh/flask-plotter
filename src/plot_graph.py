import matplotlib.pyplot as plt
import numpy as np
import io

def plot(data_in_json):

    try:
        x = np.array(data_in_json["time"])
        y = np.array(data_in_json["measurements"])
    except:
        return {'ERROR': 'Unmatching JSON keys'}

    try:
        back = plt.imread("src/static/gestation.png")
        fig, ax = plt.subplots()
        plt.scatter(x, y, s=100 , c='r', marker='x', linewidths=1)
        ax.imshow(back, extent=[23, 42, 17, 39])

        img = io.BytesIO()
        fig.savefig(img, bbox_inches='tight', format='png', dpi=400)
        plt.close(fig)
        return img
    except:
        return {'ERROR': 'Problem arised during plotting'}

