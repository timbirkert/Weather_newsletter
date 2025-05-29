import requests
import datetime

def Wetter_check(Ort):
    # API-Schlüssel (ersetze durch deinen eigenen Schlüssel)
    api_key = "49cc3e7778586f1221bf6f08992e2d3f"
    # Stadt, für die du das Wetter abrufen möchtest
    city = Ort
    # Basis-URL der OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        # Anfrage an die API senden
        response = requests.get(url)
        response.raise_for_status()  # Fehlerprüfung
        data = response.json()

        # Wetterdaten extrahieren
        wetter_beschreibung = data["weather"][0]["description"].capitalize()
        temperatur = data["main"]["temp"]
        gefuehlte_temp = data["main"]["feels_like"]
        luftfeuchtigkeit = data["main"]["humidity"]
        regenwahrscheinlichkeit = data.get("rain", {}).get("1h", 0)  # Regen in mm der letzten Stunde (falls vorhanden)
        windgeschwindigkeit = data["wind"]["speed"]
        sonnenaufgang = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M')
        sonnenuntergang = datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M')

        # Wetterbericht ausgeben
        antwort = ""
        antwort+=f"Wetterbericht für {city}:"
        antwort+=f"Beschreibung: {wetter_beschreibung}"
        antwort+=f"Temperatur: {temperatur}°C (Gefühlt: {gefuehlte_temp}°C)"
        antwort+=f"Luftfeuchtigkeit: {luftfeuchtigkeit}%"
        antwort+=f"Regen (letzte Stunde): {regenwahrscheinlichkeit} mm"
        antwort+=f"Windgeschwindigkeit: {windgeschwindigkeit} m/s"
        antwort+=f"Sonnenaufgang: {sonnenaufgang} Uhr"
        antwort+=f"Sonnenuntergang: {sonnenuntergang} Uhr"

    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen der Wetterdaten: {e}")

    return antwort

def Wetter_check_simple():
    import requests

    # API-Schlüssel (ersetze durch deinen eigenen Schlüssel)
    api_key = "49cc3e7778586f1221bf6f08992e2d3f"
    # Stadt, für die du das Wetter abrufen möchtest
    city = "Bayreuth"
    # Basis-URL der OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        # Anfrage an die API senden
        response = requests.get(url)
        response.raise_for_status()  # Fehlerprüfung
        data = response.json()

        antwort=""

        # Wetterdaten ausgeben
        antwort+=f"Wetter in {city}:"
        antwort+=f"Temperatur: {data['main']['temp']}°C"
        antwort+=f"Gefühlt: {data['main']['feels_like']}°C"
        antwort+=f"Luftfeuchtigkeit: {data['main']['humidity']}%"
        antwort+=f"Wetter: {data['weather'][0]['description'].capitalize()}"
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen der Wetterdaten: {e}")

        return (antwort)