import os
import sys
import copy
import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), './pylibs'))
import requests
import bs4

OPTION_METADATA = "--metadata"


def fetch(urls, metadata=False):

    # check urls are specified or not
    if len(urls) == 0:
        print("No urls are specified.")

    for url in urls:
        print("site: %s" % url)

        # check url format
        if url.startswith("http") is False:
            print("Error occured. Invalid url: %s" % url)
            continue

        # get domain name as file name
        strs = url.split("/")
        if len(strs) > 2:
            file_name = strs[2] + ".html"
        else:
            print("Error occured. Invalid url: %s" % url)
            continue

        try:
            # fetch html
            site_data = requests.get(url)
        except Exception as ex:
            print("Failed to request html.")
            print(ex)
            continue

        with open(file_name, "w", encoding='utf-8', errors='ignore') as f:
            # save data as html
            f.write(site_data.text)

            # print metadata
            if metadata:
                soup = bs4.BeautifulSoup(site_data.text,  'html.parser')
                print("num of links: %s" % len(soup.find_all('a')))
                print("num of images: %s" % len(soup.find_all('img')))
                print("last fetch at: %s" % datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

        print("saved html as \"%s\"" % file_name)


def main():

    args = copy.copy(sys.argv)

    # get metadata option
    metadata = OPTION_METADATA in args
    if metadata:
        args.remove(OPTION_METADATA)

    # get urls
    urls = []
    for num in range(1, len(args)):
        urls.append(args[num])

    try:
        fetch(urls, metadata)
    except Exception as ex:
        print("Error has occured.")
        print(ex)


if __name__ == '__main__':
    main()
