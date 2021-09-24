# ia_torrent

ia_torrent retrieves torrent files corresponding to a search request on the Internet Archive.

## Basic setup

Install the requirements:
```
$ pip install -r requirements.txt
```

# Run the application:
```
$ python -m ia_torrent --help
$ python -m ia_torrent <search request>
$ python -m ia_torrent <search request> --folder [folder]
```
For instance:
```
python ia_torrent.py 'collection:cdromsoftware AND subject:Microsoft'
```