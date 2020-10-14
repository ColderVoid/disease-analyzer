"""

How to print progress bar:

# A List of Items
    items = list(range(0, 57))
    l = len(items)

    # Initial call to print 0% progress
    printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)

And remember not to remove 'def printProgressBar'!

"""

import time
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


if __name__ == "__main__":

    log = []
    url = "https://services1.arcgis.com/YmCK8KfESHdxUQgm/arcgis/rest/services/KoronawirusPolska_czas_widok" \
          "/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects" \
          "&outFields=*&orderByFields=Aktualizacja%20asc&resultOffset=0&resultRecordCount=32000&resultType=standard" \
          "&cacheHint=true "

    with urllib.request.urlopen(url) as worker:
        worker = worker.read()
        # I'm guessing this would output the html source code ?
        json_code = json.loads(worker)
        print(worker)

        print("--------")
        print(json_code["features"])

        worker2 = json_code["features"]

        for row in worker2:
            print("row attrib " + str(row))
            # print(worker2[row])
