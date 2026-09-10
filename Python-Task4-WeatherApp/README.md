# Nova Weather app
-This python project developed is used to fetch the weather data of the city entered in the blank by using the weather API.
## Features
- Enter city name.
- Fetch real-time weather using the OpenWeatherMap API.
- Display:
  - Temperature (°C)
  - Humidity
  - Weather Condition
  - Wind Speed
- Handles invalid city names and network errors.
## Technologies Used
- Python
- Flask
- Requests
- OpenWeatherMap API
## To Run the Project through bash
```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## API Key
Replace `YOUR_API_KEY` in `app.py` with your free OpenWeatherMap API key.