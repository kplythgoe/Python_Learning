import requests
import datetime as dt
import os

APPLICATION_ID = os.environ["APPLICATION_ID"]
API_KEY = os.environ["API_KEY"]

exercises = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": API_KEY
}

exercise_options = {
    "query": exercises
}

response = requests.post(url=f"https://trackapi.nutritionix.com/v2/natural/exercise", json=exercise_options,
                         headers=headers)

exercise_data = response.json()
now = dt.datetime.now()


workouts = {
    "workout": {
        "date": now.strftime("%d/%m/%Y"),
        "time": f"{now.hour}:{now.minute}:{now.second}",
        "exercise": exercise_data["exercises"][0]["user_input"].capitalize(),
        "duration": exercise_data["exercises"][0]["duration_min"],
        "calories": exercise_data["exercises"][0]["nf_calories"]
    }
}

sheety_headers = {
    "Authorization": f"Bearer {os.environ["TOKEN"]}"
}

response2 = requests.post(url=os.environ["SHEET_ENDPOINT"], json=workouts, headers=sheety_headers)
print(response2.text)

