
#Steps:
#1. understand api (http protocol --> get, post, put, delete)
#2. convert python script to api--> flask framework
#3. Deploy application to server
#4. Creating github webhook
#5. condition handling -->if condition --> (/jira)


from flask import Flask, request, jsonify
import requests
import json
from requests.auth import HTTPBasicAuth  # Import HTTPBasicAuth

app = Flask(__name__)

JIRA_URL = "https://lavanyam1499.atlassian.net/rest/api/3/issue"  # Correct JIRA issue URL
JIRA_USER = "lavanyam1499@gmail.com"
JIRA_API_TOKEN = "ATATT3xFfGF0-9p28VZSt281wXdiP4UFFXmdJCLS8eWhV9BsdsbD5Rzj81479f2bVSsaeGynzNWAKvWN8CMSGqxkLMo1lJ5GcOZmVP2lfhLH75LPJ6GY-ydhJrhQ5PkD-kEa-GZHwsEBF-Cc6y4vHnxxHtfwo48tmH2o4mRdU8_7Jr_rYPcLNRE=08AFC143"

JIRA_PROJECT_KEY = "SCRUM"  # Replace with your actual JIRA project key
AUTH = HTTPBasicAuth(JIRA_USER, JIRA_API_TOKEN)

def create_jira_issue(title, description):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "fields": {
            "project": {
                "key": JIRA_PROJECT_KEY  # Ensure this matches your project key
            },
            "summary": title,  # Use the title from GitHub issue
            "description": description,  # Use the body from GitHub issue
            "issuetype": {
                "name": "Task"  # Adjust the issue type as needed (e.g., Story, Bug)
            }
        }
    }

    # Sending the request
    response = requests.post(
        JIRA_URL,
        json=payload,
        headers=headers,
        auth=AUTH
    )

    return response.json()

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    data = request.get_json()

    if 'issue' in data:
        issue_title = data['issue']['title']
        issue_body = data['issue']['body']

        # Create JIRA issue
        jira_response = create_jira_issue(issue_title, issue_body)
        # Check the response from JIRA and return a message
        if 'errorMessages' not in jira_response:
            return jsonify({"message": "JIRA issue created", "jira_response": jira_response}), 200
        else:
            return jsonify({"message": "Error creating JIRA issue", "jira_response": jira_response}), 400

    return jsonify({"message": "No issue data in the request"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)

                                                                         



'''curl -X POST http://3.82.229.116:5002/github-webhook -H "Content-Type: application/json" -d '{
  "issue": {
    "title": "Test Issue",
    "body": "/jira Testing webhook."
  } '''
                                                                        