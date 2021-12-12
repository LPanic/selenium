# python 3.8
import csv
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from tkinter import filedialog

#CSV Prompt für csv_filepath Variable
csv_filepath = filedialog.askopenfilename()

#CSV Daten in Array einlesen
with open(csv_filepath) as file:
    reader = csv.reader(file, delimiter=' ', quotechar='|')

    # Schleife für Array-Verarbeitung inkl. Page-Rendering
    for row in reader:
        service = Service("geckodriver.exe")
        s = webdriver.Firefox(service=service)

        # Timeout für Page-Rendering (3 Sekunden)
        s.set_page_load_timeout(3)
        try:
            s.get(row[0])
            time.sleep(3)

        #Exception für den Fall, dass dein Fehler auftritt
        except Exception:
            print(row[0] + " failed")

        s.close()
