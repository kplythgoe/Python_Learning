from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
            "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHQ2ZGYyMXF1bjFnMHZrcmQxem9raDU4MmJ5MjJoZG5wZ3h5M2lqMyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/S5s9Y7dqJgBLW/giphy.gif' width=300>"


random_number = random.randint(0, 9)


@app.route('/<int:number>')
def guess(number):
    result = ""
    img = ""
    if number < random_number:
        result = "WRONG - You're too low"
        img = "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmx2YjQ2ODhtdzM3cGo2YmduZGlwYnJ3bHQ0MHZ4dGJrYnh2b2dkcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/EtB1yylKGGAUg/giphy.gif' width=300>"
    elif number > random_number:
        result = "WRONG - You're too high"
        img = "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmx2YjQ2ODhtdzM3cGo2YmduZGlwYnJ3bHQ0MHZ4dGJrYnh2b2dkcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/bcEKH8GjRJovm/giphy.gif' width=300>"
    else:
        result = "Congratulations, you got the right number!"
        img = "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTRkcXdxYzA5cTY1dDNxcnJrOGxsem9uc2N4Y240azhqbDNjYXZ3MyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/R312C3MEVg4SCYAber/giphy.gif' width=300>"
    return (f"<h1>{result}</h1>"
            f"{img}")


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)