import urllib.request
import json

def main():
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib.request.urlopen(urlData)
    print("Result Code : "+str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Recieved an error from server, cannot print results", webUrl.getcode())

if __name__ == "__main__":
    main()