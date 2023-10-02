import threading
import time
from dataclasses import dataclass
import requests
from temporalio import activity

WEBHOOK_URL = 'WEBHOOK_URL'  # Replace with your actual webhook URL


@dataclass
class YourParams:
    greeting: str
    name: str


@activity.defn
def compose_greeting(input: YourParams) -> str:
    if activity.info().attempt < 2:
        print(
            f"Heartbeating activity on thread {threading.get_ident()} | attempt number {activity.info().attempt}"
        )

        activity.heartbeat()
        time.sleep(1)

            # Always raise exception
    raise RuntimeError(f"Greeting exception: {input.greeting}, {input.name}!")



@activity.defn
def slack_notification(input: YourParams) -> str:
    print(f"Heartbeating activity on thread {threading.get_ident()}")
    activity.heartbeat()

    message = f"Notification sent to slack channel: {input.greeting} {input.name}!"
    payload = {
        'error': message
    }

    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code != 200:
        raise ValueError(
            f"Request to slack returned an error {response.status_code}, the response is:\n{response.text}"
        )
    return message