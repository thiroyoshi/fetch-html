# fetch html

Fetch the HTML of the specifeid URL.

## Dependencies

* Python 3.x

## Install and Execute locally

### Install

You can install the app as command line tool.
```
pip install -e .
```

## Execute

without options
```
fetch https://www.google.com

# logs
site: https://www.google.com
saved html as "www.google.com.html"
```

- You can get the HTML file at the path where the command was executed.

-with option `--metadata`
```
fetch --metadata https://www.google.com

# logs
site: https://www.google.com
num of links: 18
num of images: 2
last fetch at: 2022/02/08 04:40:21
saved html as "www.google.com.html"
```


## Build Container Image and Execute

### Build 

```
docker build . -t fetch-html
```

### Execute

```
docker run fetch-html --metadata https://www.google.com
```

Log output is the same as local execution.

### Get HTML file
```
docker cp <Container ID>:/app/www.google.com.html .
```


## Authors

Contributors names and contact info

- [@thiroyoshi](https://thilog.com/)

## Version History

* 0.1
    * Initial Release

