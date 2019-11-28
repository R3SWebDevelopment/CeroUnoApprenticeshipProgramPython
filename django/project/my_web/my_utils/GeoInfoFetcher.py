import requests


def fetch_country():
    resp = requests.get("https://geo-info.co/MX")
    json = resp.json()
    for index, item in enumerate(json):
        print(index)
        print(item)
