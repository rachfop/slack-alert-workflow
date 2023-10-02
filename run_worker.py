import asyncio
from concurrent.futures import ThreadPoolExecutor

from temporalio.client import Client
from temporalio.worker import Worker

from activities import compose_greeting, slack_notification
from workflows import SayHello, SayError


async def main():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="my-task-queue",
        workflows=[SayHello, SayError],
        activities=[compose_greeting, slack_notification],
        activity_executor=ThreadPoolExecutor(5),
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
