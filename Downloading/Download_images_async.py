import aiohttp
import asyncio
import os
import re
from PIL import Image
from pymongo import MongoClient

client = MongoClient(port=25055)

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

def write_metadata(file_name, url):

        image = Image.open(file_name)
        width, height = image.size
        print("Width, Height = {0}, {1}".format(width, height))

        db = client.images
        mt = db.metadata
        
        data = {
            'file': file_name,
            'width': width,
            'height': height,
            'url' : url
        }

        result = mt.insert_one(data)
        print('Image data: {0}'.format(result.inserted_id))

 
async def download_image(session, url):
    async with session.get(url) as response:
        filename = os.path.basename(url)

        print("Start downloading {0}..".format(filename), end=" ")

        with open(filename, 'wb') as f_handle:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                f_handle.write(chunk)

        print("Done.")

        try:
            write_metadata(filename, url)
        except Exception as exc:
            print("Failed to save metadata: {0}".format(exc))

        return await response.release() 
 
async def main(loop):
    urls = [
        "http://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg",
        "https://steptosea.com/wp-content/uploads/2018/03/realty/1749/432d4a9ae31b30e5fab92c84db17fce1.JPG"
    ]
 
    async with aiohttp.ClientSession(loop=loop) as session:

        for url in urls:

            if not validate_url(normalize_url(url)):
                print("Url '{0}' is not valid. Skipping...".format(url))
                continue

            await download_image(session, url)
 
 
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))