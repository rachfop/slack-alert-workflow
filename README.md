# README for Temporal Slack Notification Application

## Overview

This Temporal application demonstrates the use of activities and workflows to send error notifications to Slack.

The primary goal is to attempt an activity (`compose_greeting`), and if it fails, send an alert to Slack detailing the error.

## Components

### Activities

1. **compose_greeting**: This activity takes a greeting and a name as input and simulates an activity that will always fail. It also has logic to heartbeat to Temporal and sleep for a second before failing. This is used to show the retry capabilities of Temporal.

2. **slack_notification**: This activity is designed to send error messages to a specific Slack channel using a webhook. If there's a problem sending the message to Slack, this activity will raise an exception.

### Workflows

1. **SayHello**: This workflow tries to execute the `compose_greeting` activity. The activity is set to retry up to 2 times with a timeout of 5 seconds.

2. **SayError**: This workflow is designed to be called when the `SayHello` workflow encounters an exception. It will execute the `slack_notification` activity to send an error message to Slack.

### Main Execution Logic

The primary execution logic first attempts to run the `SayHello` workflow. If it encounters an exception, it then runs the `SayError` workflow to alert Slack of the error.

## How to Run

1. Ensure you have Temporal server running locally.

2. Start the Temporal worker by executing:

```bash
poetry run python run_worker.py
```

This worker listens for tasks from the Temporal server and executes the workflows and activities as required.

3. Execute the main application:

```bash
poetry run python run_workflow.py
```

This will start the `SayHello` workflow. Since the `compose_greeting` activity is designed to always fail, the exception will be caught, and the `SayError` workflow will be triggered, sending an error notification to Slack.

## Important Note

Ensure to replace the `WEBHOOK_URL` in the activities file with your actual Slack webhook URL. Remember to keep this webhook URL private and secure, as anyone with access to it can post messages to your Slack channel.

## Dependencies

- temporalio
- requests

Ensure these are installed in your environment before running the application.

```bash
poetry install
```
