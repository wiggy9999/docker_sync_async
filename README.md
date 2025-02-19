# Kommunikation mit Docker

## Voraussetzungen
- Docker und Docker Compose installiert

## Setup
1. Repository klonen: `git clone <URL>`
2. In das Verzeichnis wechseln: `cd <projektname>`
3. Container starten: `docker-compose up --build -d`

## Synchrone Kommunikation testen
1. Terminal öffnen und ausführen:

```docker exec -it worker python /scripts/sync_request.py```

2. Ergebnis beobachten (z.B. "Antwort von Nginx: 200").

## Asynchrone Kommunikation testen
1. Terminal 1: Consumer starten

```docker exec -it worker python /scripts/async_receive.py```

2. Terminal 2: Nachricht senden

```docker exec -it worker python /scripts/async_send.py```

3. Im ersten Terminal die empfangene Nachricht sehen (z.B. "Hallo, Welt!").

## Beenden
- Container stoppen: `docker-compose down`
