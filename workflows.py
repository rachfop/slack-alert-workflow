from datetime import timedelta

from temporalio import workflow
from temporalio.common import RetryPolicy
import logging

# Import our activity, passing it through the sandbox
with workflow.unsafe.imports_passed_through():
    from activities import YourParams, compose_greeting, slack_notification


@workflow.defn
class SayHello:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            compose_greeting,
            YourParams("Hello", name),
            schedule_to_close_timeout=timedelta(seconds=5),
            retry_policy=RetryPolicy(maximum_attempts=2)
        )

@workflow.defn
class SayError:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            slack_notification,
            YourParams("You have the following error:", name),
            schedule_to_close_timeout=timedelta(seconds=5),
        )