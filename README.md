# python-fast-api: FastAPI with Python

This is a boilerplate API with FastAPI & Python to create todo items on a list

## Authors

-   [@alluster](https://www.github.com/alluster)

## Installation

First Start a new Python virtual environment on your machine

```bash
	$ cd python-fast-api
	$ python3 -m venv .venv
	$ source .venv/bin/activate
	$ pip install fastapi
	$ pip install uvicorn
```

## Running locally

```bash
    $ cd python-fast-api
    $ uvicorn main:app --reload
```

To view Swagger UI of the API navigate to:

```bash
  localhost:8000/docs#
```

## API Reference

API address is:

```http
  http://localhost:8000/api/
```

#### Get all items

```http
  GET /items
```

| Parameter | Type  | Required |  Default |
| :-------- | :---- | :------- | :------- |
| `limit`   | `int` | `true`   |          |

#### Get item

```http
  GET /items/{item_id}
```

#### Add item

```http
  POST /items
```

| Parameter | Type      | Required |  Default |
| :-------- | :-------- | :------- | :------- |
| `text`    | `string`  | `true`   |          |
| `is_done` | `boolean` | `false`  | `false`  |
