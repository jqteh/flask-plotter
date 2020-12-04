import matplotlib.pyplot as plt
import json
import numpy as np

def plot(data_in_json):

    try:
        x = np.array(data_in_json["Felipe"]["time"])
        y = np.array(data_in_json["Felipe"]["measurements"])
    except:
        return {'ERROR': 'Unmatching JSON keys'}

    try:
        img = plt.imread("src/static/gestation.png")
        fig, ax = plt.subplots()
        plt.scatter(x, y)
        ax.imshow(img, extent=[23, 42, 17, 39])
    
        fig.savefig('src/bin/figure.png')
        plt.close(fig)
    except:
        return {'ERROR': 'Problem arised during plotting'}

    return {'Message': 'Success'}
