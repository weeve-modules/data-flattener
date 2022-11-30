# Data Flattener

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | Data Flattener                           |
| Version        | v1.0.0                                |
| DockerHub | [weevenetwork/data-flattener](https://hub.docker.com/r/weevenetwork/data-flattener) |
| Authors        | Jakub Grzelak                   |

- [Data Flattener](#data-flattener)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Flatten your nested data. Use the following symbols for indicating parentness in your nested data, i.e. if parentness is `/` then data `{'location': {'city': 'Berlin'}}` will be flattened to `{'location/city': 'Berlin'}`. If data contains a list of JSON objects then each object will be given a numeric index in the new label in the flattened output (see a list example in [Output](#output))

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                 | Environment Variables     | type     | Description                                              |
| -------------------- | ------------------------- | -------- | -------------------------------------------------------- |
| Delimiter    | DELIMITER         | string   | Symbol for indicating parentness delimiter in your nested data, i.e. if delimiter is `/` then data `{'location': {'city': 'Berlin'}}` will be flattened to `{'location/city': 'Berlin'}`            |



### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)  |
| EGRESS_URLS            | string | HTTP ReST endpoints for the next module         |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
requests
```

## Input

Input to this module is:

* JSON body single object, example:

```json
{
    "employees": [
        {
            "name": {
                "first-name": "Ram",
                "family-name": "Blue"
            },
            "email": "ram@gmail.com",
            "age": 23
        },
        {
            "name": {
                "first-name": "Shyam",
                "family-name": "Red"
            },
            "email": [
                {
                    "address": "shyam23@gmail.com",
                    "type": "business"
                }
            ],
            "age": 28
        }
    ]
}

```

* array of JSON body objects, example:

```json
[
    {
        "location": {
            "city": "Berlin",
            "country": "Germany"
        }
    },
    {
        "device": {
            "name": "RaspberryPi",
            "id": "dasc4d4a"
        }
    }
]
```

## Output

If `DELIMITER = /` then output of this module is:

* JSON body single object, example:

```json
{
    "employees/0/name/first-name": "Ram",
    "employees/0/name/family-name": "Blue",
    "employees/0/email": "ram@gmail.com",
    "employees/0/age": 23,
    "employees/1/name/first-name": "Shyam",
    "employees/1/name/family-name": "Red",
    "employees/1/email/0/address": "shyam23@gmail.com",
    "employees/1/email/0/type": "business",
    "employees/1/age": 28,
}

```

* array of JSON body objects, example:

```json
[
    {
        "location/city": "Berlin",
        "location/country": "Germany"
    },
    {
        "device/name": "RaspberryPi",
        "device/id": "dasc4d4a"
    }
]
```
