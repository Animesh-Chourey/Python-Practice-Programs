import urllib.request

def main():
    weburl = urllib.request.urlopen("http://www.google.com")
    #Return the code 200 if everything is ok otherwise 404
    print("Result COde = ",weburl.getcode())

    data = weburl.read()
    print(data)


if __name__ == "__main__":
    main()