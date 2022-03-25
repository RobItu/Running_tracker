import requests
from datetime import datetime

USERNAME = "chainlinkforthewin"
TOKEN = "bratchusesapi"
pixela_endpoint = "https://pixe.la/v1/users"
user_params= {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "fitgraph",
    "name": "Running Graph",
    "unit": "m",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()
DATE = today.strftime("%Y%m%d")
pixel_param = {
    "date": DATE,
    "quantity": "3",
}
response = requests.put(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/fitgraph/{DATE}",json=pixel_param, headers=headers)
print(response.text)
