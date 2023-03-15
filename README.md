# Rates API

Rates API is used to retrieve average rates for each day on a route between port codes *origin* and *destination*. 

## Setup

First, use pip3 to install the requirements of the API

```bash
pip install -r requirements.txt
```
Please follow the instruction given in the [setup description](https://github.com/xeneta/ratestask/tree/trunk#initial-setup) to setup the database. Create a .env file in the root folder(ratesapi/) and provide the database password as given below.

```bash
DATABASE_PASSWORD = 'provide_database_password_here'
```
Run the ratesapi by executing the following command from the root folder.

```bash
python3 api/app.py
```

## Details

Use `/rates` endpoint with the following parameters:

* date_from
* date_to
* origin
* destination

and it will returns a list with the average prices for each day on a route between port codes origin and destination. It will return an empty value (JSON null) for days on which there are less than 3 prices in total. Both the origin, destination params accept either port codes or region slugs. Therefore it is possible to query for average prices per day between geographic groups of ports. Sample curl command is given below.

    curl "http://127.0.0.1/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"
