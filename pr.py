import requests
import json

# editable section
branch = "hotfix/branch1"
bases = ["master", "dev1.1.0"]
related_rm_id = "33445"
## optional - if empty this should derive from ticket title
purpose = " this is sample pull request message"
related_jira_id = ""

# static section
ghe_uri = "https://api.github.com/repos/hyonta0329/create_pr/pulls"
redmine_server = ""
email = "pyonta.hyonta@gmail.com"
username = "hyonta0329"
api_token = ""

# section for functions
def create_message(redmine_server, related_rm_id, purpose):
    return ("RM" + related_rm_id + ": "+ purpose)
  # do nothing

def create_payload(message, username, branch, base, api_token):
    return {"title" : message, "body" : "ご確認お願いします", "head" : branch, "base" : base} 

# main logic
message = create_message(redmine_server, related_rm_id, purpose)
for base in bases:
    payload = create_payload(message, username, branch, base, api_token)
    print (payload)
    res = requests.post(
        ghe_uri,
        data=json.dumps(payload),
        headers={"Authorization": "token " + api_token}
        )
    print (res.text)
