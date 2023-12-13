# Project Title

A brief description of what this project does and who it's for.

## Installation

Install project dependencies:

```bash
pip install -r requirements.txt
```

## Usage/Examples

    ```bash

uvicorn main:app --reload

````
### API Reference

#### Get item

```http
  GET /items/${id}
````

| Parameter | Type  | Description                       |
| :-------- | :---- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of item to fetch |

#### Get all items

```http
  GET /items
```

| Parameter | Type  | Description                                                    |
| :-------- | :---- | :------------------------------------------------------------- |
| `skip`    | `int` | **Optional**. Number of items to skip. Default is 0.           |
| `limit`   | `int` | **Optional**. Limit number of items to return. Default is 100. |
