# API Documentation

This page describes all API endpoints of this project.

[← Back to README](../README.md)

> Authentication system of this project is based on JWT Tokens. For endpoints that require authentication pass the 
> token as Authorization Header. For example:  
> `Authorization: Bearer <access_token>`

## Table of Contents

- [Authentication](#authentication)  
  - [Login](#login)  
  - [Create new user](#create-new-user)  
- [User Endpoints](#user-endpoints)  
  - [User Information](#user-information)  
  - [Edit User](#edit-user)  
- [Address Endpoints](#address-endpoints)  
  - [Get address](#get-address)  
  - [Edit address](#edit-address)  
- [Item Endpoints](#item-endpoints)  
  - [Get item](#get-item)  
  - [Get items](#get-items)  
  - [Create item](#create-item)  
  - [Edit item](#edit-item)  
  - [Delete item](#delete-item)  
- [Category Endpoints](#category-endpoints)  
  - [Get categories](#get-categories)  
- [Order Endpoints](#order-endpoints)  
  - [Get order](#get-order)  
  - [Add item](#add-item)  
  - [Remove item](#remove-item)  
  - [Place order](#place-order)

## Authentication
### Login

Authenticate user and retrieve a JWT Access Token.

| URL           | Method | Requires auth | Requires superuser rights |
|---------------|--------|---------------|---------------------------|
| _/user/login_ | POST   | No            | No                        |

Request body:
```json
{
    "phone": "string",
    "password": "string"
}
```
Response:
```json
{
    "access_token": "string",
    "token_type": "bearer"
}
```

### Create new user

Register a new user in the system.

| URL            | Method | Requires auth | Requires superuser rights |
|----------------|--------|---------------|---------------------------|
| _/user/create_ | POST   | No            | No                        |

Request body:
```json
{
    "name": "string",
    "phone": "string",
    "password": "string"
}
```
Response:
```json
{
    "id": 1,
    "name": "string",
    "phone": "string",
    "password": "string",
    "address": {
        "street": null,
        "reference": null
    },
    "is_superuser": false
}
```

## User Endpoints

### User Information
Get current user's information.

| URL     | Method | Requires auth | Requires superuser rights |
|---------|--------|---------------|---------------------------|
| _/user_ | GET    | Yes           | No                        |

Response:
```json
{
    "id": 1,
    "name": "string",
    "phone": "string",
    "password": "string",
    "address": {
        "street": null,
        "reference": null
    },
    "is_superuser": false
}
```

### Edit User
Edit current user's information.

| URL     | Method | Requires auth | Requires superuser rights |
|---------|--------|---------------|---------------------------|
| _/user_ | PUT    | Yes           | No                        |

Request Body:
> All parameters are optional. You may include only the fields you want to update. Just make sure to provide at 
> least one field.
```json
{
    "name": "string",
    "phone": "string",
    "password": "string"
}
```

Response:
```json
{
    "id": 1,
    "name": "string",
    "phone": "string",
    "password": "string",
    "address": {
        "street": null,
        "reference": null
    },
    "is_superuser": false
}
```

## Address Endpoints

### Get address
Get current user's address.

| URL             | Method | Requires auth | Requires superuser rights |
|-----------------|--------|---------------|---------------------------|
| _/user/address_ | GET    | Yes           | No                        |

Response:
```json
{
    "street": "string",
    "reference": "string"
}
```

### Edit address
Edit current user's address.

| URL             | Method | Requires auth | Requires superuser rights |
|-----------------|--------|---------------|---------------------------|
| _/user/address_ | PUT    | Yes           | No                        |

Request body:
> All parameters are optional. You may include only the fields you want to update. Just make sure to provide at 
> least one field.
```json
{
    "street": "string",
    "reference": "string"
}
```

Response:
```json
{
    "street": "string",
    "reference": "string"
}
```

## Item Endpoints

### Get item
Get particular item from the menu.

| URL          | Method | Requires auth | Requires superuser rights  |
|--------------|--------|---------------|----------------------------|
| _/item/{id}_ | GET    | No            | No                         |

Response:
```json
{
    "id": 1,
    "name": "string",
    "description": "string",
    "price": 0.0,
    "image_path": "",
    "categories": [
        {
            "id": 1,
            "name": "category1"
        },
        {
            "id": 2,
            "name": "category2"
        },
        {
            "id": 3,
            "name": "category3"
        }
    ],
    "is_available": true
}
```

### Get items
Get all items in the menu.

| URL           | Method | Requires auth | Requires superuser rights  |
|---------------|--------|---------------|----------------------------|
| _/item/items_ | GET    | No            | No                         |

Request parameters:  

| Name          | Type | Description                                                                            |
|---------------|------|----------------------------------------------------------------------------------------|
| _category_id_ | int  | When this parameter is specified, only items from the given category will be returned. |

Response:
```json
[
    {
        "id": 1,
        "name": "string",
        "description": "string",
        "price": 0.0,
        "image_path": "",
        "categories": [
            {
                "id": 1,
                "name": "category1"
            },
            {
                "id": 2,
                "name": "category2"
            },
            {
                "id": 3,
                "name": "category3"
            }
        ],
        "is_available": true
    }
]
```

### Create item

Add new item to the menu.

| URL     | Method | Requires auth | Requires superuser rights |
|---------|--------|---------------|---------------------------|
| _/item_ | POST   | Yes           | Yes                       |

Request body:
```json
{
    "name": "string",
    "description": "string",
    "price": 0.0,
    "image_path": "path/to/image",
    "categories": [
        1, 2, 3
    ]
}
```

Response: 
```json
{
    "id": 1,
    "name": "string",
    "description": "string",
    "price": 0.0,
    "image_path": "",
    "categories": [
        {
            "id": 1,
            "name": "category1"
        },
        {
            "id": 2,
            "name": "category2"
        },
        {
            "id": 3,
            "name": "category3"
        }
    ],
    "is_available": true
}
```

### Edit item
Edit item's information.

| URL          | Method | Requires auth | Requires superuser rights |
|--------------|--------|---------------|---------------------------|
| _/item/{id}_ | PUT    | Yes           | Yes                       |

Request body:
> All parameters are optional. You may include only the fields you want to update. Just make sure to provide at 
> least one field.
```json
{
  "name": "string",
  "description": "string",
  "price": 0.0,
  "image_path": "path/to/image",
  "categories": [1, 2],
  "is_available": false
}
```

Response:
```json
{
    "id": 1,
    "name": "string",
    "description": "string",
    "price": 0.0,
    "image_path": "",
    "categories": [
        {
            "id": 1,
            "name": "category1"
        },
        {
            "id": 2,
            "name": "category2"
        }
    ],
    "is_available": false
}
```

### Delete item

| URL          | Method | Requires auth | Requires superuser rights |
|--------------|--------|---------------|---------------------------|
| _/item/{id}_ | DELETE | Yes           | Yes                       |

Response:
```json
{
    "success": true
}
```

## Category Endpoints

### Get categories
Get all menu categories.

| URL                | Method | Requires auth | Requires superuser rights |
|--------------------|--------|---------------|---------------------------|
| _/item/categories_ | GET    | No            | No                        |

Response:
```json
[
    {
        "id": 1,
        "name": "category1"
    },
    {
        "id": 2,
        "name": "category2"
    },
    {
        "id": 3,
        "name": "category3"
    }
]
```

## Order Endpoints

### Get order
Get current user's order. If current user doesn't have non-placed order, new order will be created and returned.

| URL      | Method | Requires auth | Requires superuser rights |
|----------|--------|---------------|---------------------------|
| _/order_ | GET    | Yes           | No                        |

Response:
```json
{
    "id": 1,
    "items": [
        {
            "item": {
                "id": 1,
                "name": "string",
                "description": "string",
                "price": 0.0,
                "image_path": "",
                "categories": [
                    {
                        "id": 1,
                        "name": "category1"
                    },
                    {
                        "id": 2,
                        "name": "category2"
                    }
                ],
                "is_available": true
            },
            "quantity": 1
        }
    ],
    "is_placed": false
}
```

### Add item
Add item to the order. If item is already in the order, _quantity_ field will be increased.

| URL                | Method | Requires auth | Requires superuser rights |
|--------------------|--------|---------------|---------------------------|
| _/order/add-item_  | PUT    | Yes           | No                        |

Request body:
```json
{
    "item_id": 1
}
```

Response:
```json
{
    "id": 1,
    "items": [
        {
            "item": {
                "id": 1,
                "name": "string",
                "description": "string",
                "price": 0.0,
                "image_path": "",
                "categories": [
                    {
                        "id": 1,
                        "name": "category1"
                    },
                    {
                        "id": 2,
                        "name": "category2"
                    }
                ],
                "is_available": true
            },
            "quantity": 2
        }
    ],
    "is_placed": false
}
```

### Remove item
Remove item from the order. If amount of this item in the order exceeds 1, _quantity_ field will be decreased.

| URL                  | Method | Requires auth | Requires superuser rights |
|----------------------|--------|---------------|---------------------------|
| _/order/remove-item_ | PUT    | Yes           | No                        |

Request body:
```json
{
    "item_id": 1
}
```

Response:
```json
{
    "id": 1,
    "items": [
        {
            "item": {
                "id": 1,
                "name": "string",
                "description": "string",
                "price": 0.0,
                "image_path": "",
                "categories": [
                    {
                        "id": 1,
                        "name": "category1"
                    },
                    {
                        "id": 2,
                        "name": "category2"
                    }
                ],
                "is_available": true
            },
            "quantity": 1
        }
    ],
    "is_placed": false
}
```

### Place order
Mark current user's order as placed and send it to the operator.

| URL            | Method | Requires auth | Requires superuser rights |
|----------------|--------|---------------|---------------------------|
| _/order/place_ | POST   | Yes           | No                        |

Response:
```json
{
    "id": 1,
    "items": [
        {
            "item": {
                "id": 1,
                "name": "string",
                "description": "string",
                "price": 0.0,
                "image_path": "",
                "categories": [
                    {
                        "id": 1,
                        "name": "category1"
                    },
                    {
                        "id": 2,
                        "name": "category2"
                    }
                ],
                "is_available": true
            },
            "quantity": 1
        }
    ],
    "is_placed": true
}
```
