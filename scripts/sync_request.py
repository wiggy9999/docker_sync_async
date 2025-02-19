import requests
response = requests.get("http://webserver")
print(f"Antwort von Nginx: {response.status_code}")
