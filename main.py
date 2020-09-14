import requests

if __name__ == "__main__":
    r = requests.get("https://api.ipify.org?format=json")
    print(r.text)

