import matplotlib.pyplot as plt
import json
import numpy as np

def plot(data_in_json):
    data = json.loads(data_in_json)
    x = np.array(data["Felipe"]["time"])
    y = np.array(data["Felipe"]["measurements"])

    img = plt.imread("src/static/gestation.png")
    fig, ax = plt.subplots()
    plt.scatter(x, y)
    ax.imshow(img, extent=[23, 42, 17, 39])
    
    fig.savefig('scr/bin/figure.png')
    plt.close(fig)
