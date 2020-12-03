import requests

data_in_json = """
{
    "Felipe" : {
        "time": [27, 28, 29, 30, 31, 32, 33, 34],
        "measurements": [30, 30, 31, 31.2, 33, 33.2, 33.3, 33.4]
    }
}
"""

resp = requests.post("http://localhost:5000/plotter", files={'data': data_in_json})

print(resp)