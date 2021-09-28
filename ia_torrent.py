import click
import requests
from requests.exceptions import HTTPError
import urllib.parse
from pathlib import Path
import os
import csv
import pdb

@click.command()
@click.argument('query')
@click.option('--folder', default="torrents", help='Folder in which to save torrent files.')
@click.option('--file', default="identifiers.csv", help='Save the identifier csv file.')
def search(query, folder, file):
    Path(folder).mkdir(parents=True, exist_ok=True)
    archive = "https://archive.org/advancedsearch.php?q={}&fl%5B%5D=identifier&rows=1000000000&page=1&output=csv"
    safe_string = urllib.parse.quote_plus(query)
    try:
        r = requests.get(archive.format(query))
        r.raise_for_status()

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        with open(file, 'wb+') as f:
            f.write(r.content)
        decoded_content = r.content.decode('utf-8')
        pdb.set_trace()
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        identifiers = list(cr)
        for row in identifiers:
            if row[0] != 'identifier':
                get_torrent(row[0], folder)

def get_torrent(id, folder):
    metadata_url = "https://archive.org/metadata/{}"
    try:
        req = requests.get(metadata_url.format(id))
        req.raise_for_status()

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        jresponse = req.json()
        dir = jresponse["dir"]
        ws = jresponse["workable_servers"][0]

        url = "http://{}{}/{}_archive.torrent"
        filename = "{}.torrent"

        with open(os.path.join(folder, filename.format(id)), 'wb+') as f:

            try:
                dl = requests.get(url.format(ws, dir, id))
                req.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
            except Exception as err:
                print(f'Other error occurred: {err}')
            else:
                f.write(dl.content)


if __name__ == '__main__':
    search()
