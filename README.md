# ia_torrent

ia_torrent retrieves torrent files corresponding to a search request on the Internet Archive.

## Basic setup

Install the requirements:
```
./install.sh
```

# Run the application:
```
$ . ./venv/bin/activate
$ python ia_torrent --help
$ python ia_torrent <search request>
$ python ia_torrent <search request> --folder [folder]
```
For instance:
```
python ia_torrent.py 'collection:cdromsoftware AND subject:Microsoft'
```
