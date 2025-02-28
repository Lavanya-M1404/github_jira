# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://lavanyam1499.atlassian.net/rest/api/3/issue"

API_TOKEN="ATATT3xFfGF0-9p28VZSt281wXdiP4UFFXmdJCLS8eWhV9BsdsbD5Rzj81479f2bVSsaeGynzNWAKvWN8CMSGqxkLMo1lJ5GcOZmVP2lfhLH75LPJ6GY-ydhJrhQ5PkD-kEa-GZHwsEBF-Cc6y4vHnxxHtfwo48tmH2o4mRdU8_7Jr_rYPcLNRE=08AFC143"

auth = HTTPBasicAuth("lavanyam1499@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My second JIRA ticket.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10003"
    },
    "project": {
      "key": "SCRUM"
    },
    "summary": "First JIRA ticket"
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))