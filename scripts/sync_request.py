import requests
print("Nachricht gesendet...")
print("Warte auf Antwort...")
response = requests.get("http://webserver")
print(f"Antwort von Nginx: {response.status_code}")
