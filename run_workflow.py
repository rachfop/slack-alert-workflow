import asyncio

from temporalio.client import Client

from workflows import SayHello, SayError


async def main():
    client = await Client.connect("localhost:7233")

    try:
        result = await client.execute_workflow(
            SayHello.run, "my name", id="my-workflow-id", task_queue="my-task-queue"
        )
    except Exception as err:

        result = await client.execute_workflow(
            SayError.run, str(err), id="my-workflow-id", task_queue="my-task-queue"
        )

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
