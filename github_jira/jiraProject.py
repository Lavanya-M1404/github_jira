# This code sample uses the 'requests' library:
# http://docs.python-requests.org

import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://lavanyam1499.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0-9p28VZSt281wXdiP4UFFXmdJCLS8eWhV9BsdsbD5Rzj81479f2bVSsaeGynzNWAKvWN8CMSGqxkLMo1lJ5GcOZmVP2lfhLH75LPJ6GY-ydhJrhQ5PkD-kEa-GZHwsEBF-Cc6y4vHnxxHtfwo48tmH2o4mRdU8_7Jr_rYPcLNRE=08AFC143"

auth = HTTPBasicAuth("lavanyam1499@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}



#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

response = requests.get(url, headers=headers, auth=auth)
# Pretty print the response
#issue_types = json.loads(response.text)
#print(json.dumps(issue_types, indent=4, sort_keys=True))


output = json.loads(response.text)
name = output[0]["id"]
print(name)


for i in output:
    name = i.get("name")
    print(name)







