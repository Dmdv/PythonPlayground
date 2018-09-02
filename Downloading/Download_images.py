 #!/usr/bin/env python3

import os, re
from urllib import parse
from urllib import request

def get_file_name(url):
    a = parse.urlparse(url)
    return os.path.basename(a.path)

def normalize_url(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        return 'http://' + url
    return url

def validate_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def download_image(url):
    
    if not validate_url(normalize_url(url)):
        print("Url '{0}' is not valid. Skipping...".format(url))
        return
    
    file_name = get_file_name(url)
    
    print("Downloading: {0}..".format(file_name), end=" ")
    
    request.urlretrieve(url, file_name)
    
    print("Done.")

def download_images():
        urls = [
            "http://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg",
            "https://steptosea.com/wp-content/uploads/2018/03/realty/1749/432d4a9ae31b30e5fab92c84db17fce1.JPG"
        ]

        for url in urls:
            download_image(url)


download_images()