# Rates API

Rates API is used to retrieve average rates for each day on a route between port codes *origin* and *destination*. It will return an empty value (JSON null) for days on which there are less than 3 prices in total. Both the origin, destination params accept either port codes or region slugs. Therefore it is possible to query for average prices per day between geographic groups of ports.

## Setup

First, use pip install to install the requirements of the API

```bash
pip install -r requirements.txt
```