# Libpostal python REST

## API Example

## Install

`make build`

## Run

`make run`

## Usage

### Parser

In your browser:

`http://localhost:8001/parser?address=100,main,st,buffalo,ny`

** Response **
```
[
  {
    "label": "house_number",
    "value": "100"
  },
  {
    "label": "road",
    "value": "main st"
  },
  {
    "label": "city",
    "value": "buffalo"
  },
  {
    "label": "state",
    "value": "ny"
  }
]
```

Optional parameters: language, country

`http://localhost:8001/parser?address=100,main,st,buffalo,ny&country=us`

`http://localhost:8001/parser?address=100,main,st,buffalo,ny&language=en&country=us`


### Expand

`http://localhost:8001/expand?address=100,main,st,buffalo,ny`

** Response **
```
[
  "100 main saint buffalo new york",
  "100 main saint buffalo ny",
  "100 main street buffalo new york",
  "100 main street buffalo ny"
]
```


Optional parameters: language


`http://localhost:8001/expand?address=100,main,st,buffalo,ny&language=en`


## Thanks to

https://github.com/sleekybadger/docker-libpostal

https://github.com/user94857/libpostal-rest
