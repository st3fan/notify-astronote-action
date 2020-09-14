

import os
import requests


def notify():
    headers = { "Authorization": os.getenv("ASTRONOTE_TOKEN") }
    notification = {
        "title": "Your coffee is ready",
        "body": "Double strong, double sweet."
    }
    r = requests.post("https://api.astronote.app/1/notify", headers=headers, json=notification)
    r.raise_for_status()


if __name__ == "__main__":
    notify()


