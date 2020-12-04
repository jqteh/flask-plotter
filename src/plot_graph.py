import matplotlib.pyplot as plt
import json
import numpy as np

def plot(data_in_json):
    try:
        data = json.loads(data_in_json)
    except:
        return "problem during parsing"
    
    try:
        x = np.array(data["Felipe"]["time"])
        y = np.array(data["Felipe"]["measurements"])
    except:
        return "problem with dictionary key"

    try:
        img = plt.imread("src/static/gestation.png")
        fig, ax = plt.subplots()
        plt.scatter(x, y)
        ax.imshow(img, extent=[23, 42, 17, 39])
    
        fig.savefig('src/bin/figure.png')
        plt.close(fig)
    except:
        return "problem during plotting"

    return "plotting successful"
