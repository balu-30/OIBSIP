from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

# Get your free API key from https://openweathermap.org/api
API_KEY = "740afd28f5edad70775505d33ee736e7"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>City Weather App</title>
    <style>
        ```css
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    min-height: 100vh;

    display: flex;
    justify-content: center;
    align-items: center;

    background: linear-gradient(135deg, #74ebd5, #9face6);
}

.container {
    width: 90%;
    max-width: 420px;

    background: rgba(255, 255, 255, 0.95);

    padding: 35px;

    border-radius: 20px;

    text-align: center;

    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
}

h2 {
    margin-top: 0;
    margin-bottom: 8px;

    font-size: 30px;
    color: #2c3e50;
}

.container::before {
    content: "☀️";
    display: block;
    font-size: 45px;
    margin-bottom: 10px;
}

form {
    margin-top: 25px;
}

input {
    width: 100%;

    padding: 13px 15px;

    border: 2px solid #dfe6e9;
    border-radius: 10px;

    font-size: 16px;

    outline: none;

    transition: 0.3s;
}

input:focus {
    border-color: #6c63ff;
    box-shadow: 0 0 8px rgba(108, 99, 255, 0.25);
}

button {
    width: 100%;

    margin-top: 15px;

    padding: 13px;

    border: none;
    border-radius: 10px;

    background: #6c63ff;
    color: white;

    font-size: 16px;
    font-weight: bold;

    cursor: pointer;

    transition: 0.3s;
}

button:hover {
    background: #574fd6;
    transform: translateY(-2px);
}

.weather {
    margin-top: 25px;

    padding: 22px;

    border-radius: 15px;

    background: #f7f9fc;

    text-align: left;

    border: 1px solid #e8ecf1;
}

.weather h3 {
    margin-top: 0;

    text-align: center;

    font-size: 24px;

    color: #2c3e50;
}

.weather p {
    padding: 10px 0;

    margin: 0;

    border-bottom: 1px solid #e5e8eb;

    color: #555;

    font-size: 16px;
}

.weather p:last-child {
    border-bottom: none;
}

.weather strong {
    color: #2c3e50;
}

.error {
    margin-top: 20px;

    padding: 12px;

    border-radius: 10px;

    background: #ffe6e6;

    color: #d63031;

    font-weight: bold;
}
```

    </style>
</head>

<body>

<div class="container">

    <h2>Nova Weather App</h2>

    <form method="POST">

        <input
            type="text"
            name="city"
            placeholder="Enter City Name"
            required
        >

        <button type="submit">
            Get Weather
        </button>

    </form>

    {% if weather %}

    <div class="weather">

        <h3>{{ weather.city }}</h3>

        <p><strong>Temperature:</strong> {{ weather.temp }} °C</p>

        <p><strong>Humidity:</strong> {{ weather.humidity }}%</p>

        <p><strong>Condition:</strong> {{ weather.condition }}</p>

        <p><strong>Wind Speed:</strong> {{ weather.wind }} m/s</p>

    </div>

    {% endif %}

    {% if error %}

    <div class="error">

        {{ error }}

    </div>

    {% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    weather = None
    error = None

    if request.method == "POST":

        city = request.form["city"].strip()

        if city == "":
            error = "Please enter a city name."

        else:
            url = (
                f"https://api.openweathermap.org/data/2.5/weather"
                f"?q={city}&appid={API_KEY}&units=metric"
            )

            try:
                response = requests.get(url)
                data = response.json()

                if response.status_code == 200:

                    weather = {
                        "city": data["name"],
                        "temp": data["main"]["temp"],
                        "humidity": data["main"]["humidity"],
                        "condition": data["weather"][0]["description"].title(),
                        "wind": data["wind"]["speed"]
                    }

                else:
                    error = "City does not exist. Please enter a valid city."

            except requests.exceptions.RequestException:
                error = "Network error. Please try again."

    return render_template_string(HTML, weather=weather, error=error)


if __name__ == "__main__":
    app.run(debug=True)