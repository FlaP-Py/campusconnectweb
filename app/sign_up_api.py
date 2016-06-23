import requests
import json
url = 'https://uploadnotes-2016.appspot.com/_ah/api/notesapi/v1/createProfile'
headers = {'Content-Type': 'application/json'}


def sign_up(user, form_data):
    user_profile = dict()
    user_profile["profileName"] = user.firstname + " " + user.lastname
    user_profile["collegeId"] = form_data["college"]
    try:
        user_profile["batchName"] = form_data["batch"]
        user_profile["branchName"] = form_data["branch"]
        user_profile["sectionName"] = form_data["section"]
        user_profile["gcmId"] = "worst" #form_data[""]
    except:
        pass
    user_profile["photoUrl"] = user.image_url
    user_profile["email"] = user.email

    api_call = requests.post(url, data=json.dumps(user_profile), headers=headers)
    print(api_call.json())
    return(api_call.json())
