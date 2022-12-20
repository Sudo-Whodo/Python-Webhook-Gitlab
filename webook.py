import requests 
import json

vm_name = "AHHHH-real-Monsters"


token = "idk-a-number-orsomthing"
url = "https://gitlab.com/api/v4/projects/1/trigger/pipeline"

variables = {
    "VAR_AUTO_APPLY": "true",
    "VM_NAME": vm_name    
}

data = {
    'token' : token,
    'ref' : 'main',
    'variables': variables
}

r = requests.post(url, data=json.dumps(data),headers={'Content-Type': 'application/json'} )



