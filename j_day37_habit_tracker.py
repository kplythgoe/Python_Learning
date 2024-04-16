import requests
from datetime import datetime

USERNAME = "kplythgoe"
TOKEN = "************"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

dot_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4"
}

# response = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}", json=dot_config, headers=headers)
# print(response.text)

dot_update = {
    "quantity" : "3"
}

# response = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{dot_config["date"]}", json=dot_update,
#                         headers=headers)
# print(response.text)

response = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{dot_config["date"]}", headers=headers)
print(response.text)