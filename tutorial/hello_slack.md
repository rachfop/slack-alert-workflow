# Tutorial: Setting Up a Temporal Workflow to Send Slack Error Notifications

In this tutorial, we'll set up a Temporal application that monitors workflow failures and sends real-time error alerts to Slack channels using webhooks.

## Prerequisites:

1. A working Python environment.
2. Temporal server running locally.
3. Slack workspace access to set up a webhook.

## Steps:

### 1. Set Up Your Python Environment

Ensure you have the required libraries installed:

```bash
pip install temporalio requests
```

### 2. Set Up Slack Incoming Webhook

- Navigate to `https://my.slack.com/apps/manage/custom-integrations`.
- Choose "Incoming WebHooks" and then "Add Configuration".
- Select a channel to post messages to and click "Add Incoming WebHooks Integration".
- Copy the provided Webhook URL; you'll use it to post messages to the channel.

### 3. Clone the Repository

Clone the repository (replace `your-repo-name` with the name you chose for your repo):

```bash
git clone https://github.com/rachfop/slack-alert-workflow.git
cd slack-alert-workflow
```

### 4. Update the Slack Webhook URL

In the `activities.py` file (or wherever you have the Slack activity defined), replace the placeholder webhook URL with the one you obtained from Slack:

```python
WEBHOOK_URL = 'YOUR_SLACK_WEBHOOK_URL'
```

### 5. Start the Temporal Worker

Run the worker script to start listening for tasks from the Temporal server:

```bash
python run_worker.py
```

This will initialize the worker and it will start listening for tasks on the specified task queue.

### 6. Run the Application

Execute the main application script:

```bash
python run_workflow.py
```

Given that the `compose_greeting` activity is designed to fail, the `SayError` workflow should be triggered and send an error notification to your Slack channel.

### 7. Verify Slack Notification

Check the Slack channel you set up for the webhook. You should see an error notification sent by your application.

## Conclusion

You've now successfully set up a Temporal application that monitors workflow failures and sends error notifications to a Slack channel. This can be expanded to include other workflows, more detailed error messages, or integrations with other platforms.

Remember to always keep your Slack webhook URL secure. Avoid exposing it in public repositories or sharing it unnecessarily, as anyone with the URL can post messages to your Slack channel. Consider using environment variables or other secure methods to store this and other sensitive information.