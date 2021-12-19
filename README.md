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

## Anleitung
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
 
## Dauer der Tests

 <br />
 
Nach Auswahl der Datenbasis startet die Verarbeitung der Domains innerhalb der CSV-Dateien:
 <br />
- Top500 Domains: Dauer ca. 27 Minuten
- Hardcore-Liste: Dauer ca. 7 Minuten
