# intranet-file-explorer
A web ui tool for transfering files between intranet machines.

> **Warning**
> this is just a dev tool, not suitable for PRODUCTION ENVIRONMENT !
>

## Background
In intranet environment, we often need to transfer files. 
[rsync](https://linux.die.net/man/1/rsync) is a good choice. 

But using a simple server is more suitable for some situations. 

Aside from usage consideration, implementing tools on our own is also a motivation.

## Key Features
- [x] Listing files in specified directory(where the server started)
- [x] Download a file by clicking
- [x] Upload multiple files with file button or dragdrop move 

## Usage
### Prerequisite
You should setup your `Python` `Pip` environment first.

And download this repo on the file's destination machine's directory.

### Start this tool server
install related dependency
```shell script
sh install.sh
```

start server
```shell script
python3 app.py -p 5000
```
or 
```shell script
sh start.sh
```

### Dispose files
You can find uploaded files in `upload` dir. 
