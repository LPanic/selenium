# Selenium Automation Script
 <br />
 
![image](https://user-images.githubusercontent.com/62666957/146691725-aaba63e7-8138-47b7-a6e2-e8bae6973712.png)

## Punkt 1 - Voraussetzungen
 <br />
Um die Ergebnisse im eigenen Netzwerk nachvollziehen zu können, wird vorausgesetzt, dass folgende Bedingungen gegeben sind:
 <br />
 <br />
 
- Python 3.8 Installation: https://www.python.org/downloads/release/python-380/
- Bestehende Installation einer Pi-Hole Instanz: https://www.smarthomebeginner.com/pi-hole-setup-guide/
- PADD für die Auswertung der Daten: https://learn.adafruit.com/pi-hole-ad-pitft-tft-detection-display/install-padd
<br />

## Punkt 2 - Anleitung

 <br />
 
- Sicherstellen, dass alle Voraussetzungen unter "Punkt 1" erfüllt sind.
- Repository klonen oder herunterladen.
- Falls noch nicht vorhanden, die neueste Firefox-Version herunterladen: https://www.mozilla.org/de/firefox/new/
- Nach der Installation von Firefox, zum geklonten Repository navigieren.
- selenium_automation.py Script mit python starten.
- Mithilfe der CSV-Prompt den gewünschten Datensatz auswählen.
- CSV_ch_top500_Nov_2021.csv - Beinhaltet die Top 500 Domains vom November 2021.
- CSV_Hardcore-Test.csv - Beinhaltet eine Sammlung von Domains, welche bekannte Tracker einsetzen. 90% dieser Domains sollten von Pi-Hole blockiert werden:

 <br />
 <br />
  
![image](https://user-images.githubusercontent.com/62666957/146691829-34a180d2-f5b9-4327-b532-a23ccc82ce58.png)

 <br />
 
## Punkt 3 - Dauer der Tests

 <br />
 
Nach Auswahl der Datenbasis startet die Verarbeitung der Domains innerhalb der CSV-Dateien:
 <br />
- Top500 Domains: Dauer ca. 27 Minuten
- Hardcore-Liste: Dauer ca. 7 Minuten
 <br />
 
## Punkt 4 - Aktivierung / Deaktivierung von Pi-Hole via API-Call
<br />
Um die Ergebnisse vergleichen zu können, kann mithilfe der folgenden API-Calls die Blockierung aktiviert bzw. deaktiviert werden:
<br />
<br />
Zum Deaktivieren: http://pi.hole/admin/api.php?disable&auth=PWHASH
<br />
Zum Aktivieren: http://pi.hole/admin/api.php?enable&auth=PWHASH
<br />
<br />

Dabei ist PWHASH der Wert von WEBPASSWORD in /etc/pihole/setupVars.conf :
<br />
<br />

![image](https://user-images.githubusercontent.com/62666957/146693102-9da6cbd2-a25b-486e-adac-bf1dfedfaeef.png)

 <br />

## Punkt 5 - Rücksetzung der Datenbank
<br />
Da PADD für die Auswertungen auf die Pi-Hole Datenbank zurückgreift, muss diese nach den jeweiligen Tests zurückgesetzt werden. 
<br />
Dies kann durch die folgenden Script ausgeführt werden:
<br />
<br />

```
cd /etc/pihole
sudo service pihole-FTL stop
sudo mv pihole-FTL.db pihole-FTL.db.old
sudo service pihole-FTL start
```

## Punkt 6 - Auswertung

<br />

Die Auswertung der Daten kann entweder direkt über http://pi.hole/admin im LAN geprüft werden:

<br />

![image](https://user-images.githubusercontent.com/62666957/146693761-33efe862-3afb-4962-80c3-53ceabd7ff5c.png)

<br />

Auswertung via PADD-Script: Hierfür eine SSH Verbindung zum lokalen Pi-Hole DNS-Resolver aufbauen und mit dem Kommando "bash padd.sh" die Auswertung aufzurufen:

<br />

![image](https://user-images.githubusercontent.com/62666957/146693680-134dd605-3112-4361-8f56-0d78874ad958.png)


