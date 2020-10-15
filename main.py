"""

How to print progress bar:

# A List of Items
    items = list(range(0, 57))
    l = len(items)

    # Initial call to print 0% progress
    printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)

And remember not to remove 'def printProgressBar'!

"""
# import section
from datetime import datetime
import time
import sys
import urllib
import urllib.request
import json


# Print iterations progress
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


# Kod do zamiany daty na dni tygodnia
# Ciekawostka, tak sie robi metode switch w pythonie. Normalnie jej nie ma
def week(i):
    switcher = {
        0: 'Niedziela',
        1: 'Poniedzialek',
        2: 'Wtorek',
        3: 'Sroda',
        4: 'Czwartek',
        5: 'Piatek',
        6: 'Sobota'
    }

    return switcher.get(i, "Unknown")


# Główna część programu
if __name__ == "__main__":
    counter = 0

    # Aktualnie open jest w trybie dodawania kolejnych lini aby to zmienić zmien 'a' na 'w'
    save = open('output2.txt', 'a')
    url = "https://services1.arcgis.com/YmCK8KfESHdxUQgm/arcgis/rest/services/KoronawirusPolska_czas_widok" \
          "/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects" \
          "&outFields=*&orderByFields=Aktualizacja%20asc&resultOffset=0&resultRecordCount=32000&resultType=standard" \
          "&cacheHint=true "

    poniedzialek = []
    wtorek = []
    sroda = []
    czwartek = []
    piatek = []
    sobota = []
    niedziela = []

    # Dostanie JSON ze strony
    with urllib.request.urlopen(url) as worker:
        worker = worker.read()
        # I'm guessing this would output the html source code ?
        json_code = json.loads(worker)

    # Wypisanie interesujących danych z json
    while counter < len(json_code['features']):
        numer_zgloszenia = json_code['features'][counter]['attributes']['nr']

        timestamp_json = str(json_code['features'][counter]['attributes']['Aktualizacja'])
        timestamp = int(timestamp_json[:-3])
        date = datetime.fromtimestamp(timestamp)
        day_of_week = datetime.fromtimestamp(timestamp).strftime('%w')
        data_zgloszenia = date

        potwierdzone_zakazenia = json_code['features'][counter]['attributes']['Potwierdzone']
        zgony = json_code['features'][counter]['attributes']['Smiertelne']
        wyleczonych = json_code['features'][counter]['attributes']['Wyleczone']
        przyrost_dzienny = json_code['features'][counter]['attributes']['Dziennie_potwierdzone']
        zgony_dziennie = json_code['features'][counter]['attributes']['Dziennie_śmiertelne']

        # Dodanie danych do pliku
        print('--------------', file=save)
        print('', file=save)
        print('Numer zgloszenia: ', numer_zgloszenia, file=save)
        print('Data zgloszenia: ', data_zgloszenia, ' ( ', week(int(day_of_week)), ' )', file=save)
        print('Potwierdzone zakazenia: ', potwierdzone_zakazenia, file=save)
        print('Zgony: ', zgony, file=save)
        print('Wyleczonych: ', wyleczonych, file=save)
        print('', file=save)
        print('Przyrost dzienny zakazen: ', przyrost_dzienny, file=save)
        print('Zgony dziennie: ', zgony_dziennie, file=save)
        print('', file=save)
        print('--------------', file=save)
        print('', file=save)

        # Wypisanie danych w konsoli
        print('--------------')
        print('')
        print('Numer zgloszenia: ', numer_zgloszenia)
        print('Data zgloszenia: ', data_zgloszenia, ' ( ', week(int(day_of_week)), ' )')
        print('Potwierdzone zakazenia: ', potwierdzone_zakazenia)
        print('Zgony: ', zgony)
        print('Wyleczonych: ', wyleczonych)
        print('')
        print('Przyrost dzienny zakazen: ', przyrost_dzienny)
        print('Zgony dziennie: ', zgony_dziennie)
        print('')
        print('--------------')
        print('')

        counter += 1

    # Zamkniecie edycji pliku
    save.close()
