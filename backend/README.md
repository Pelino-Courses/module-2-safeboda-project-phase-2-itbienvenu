# SafeBoda Project - Phase 2: Core API

![Django](https://img.shields.io/badge/Django-5.2-green) ![DRF](https://img.shields.io/badge/DRF-3.16-blue)

This repository contains the backend API for the **SafeBoda project**, built with **Django** and **Django REST Framework (DRF)**. The API allows managing users and trips, supporting full CRUD operations while ensuring security and validation rules.

---

## Table of Contents

1. [Features](#features)
2. [Setup](#setup)
3. [Models](#models)
4. [Serializers](#serializers)
5. [Views](#views)
6. [URLs / Endpoints](#urls--endpoints)
7. [Testing with Postman](#testing-with-postman)
8. [Security & Validation](#security--validation)

---

## Features

* Custom user model (`CustomUser`) with `user_type` (Rider / Driver)
* Trip management with `rider`, `driver`, `pickup_location`, `dropoff_location`, `status`, and timestamps
* Full CRUD API endpoints for users and trips
* Passwords are **write-only** to prevent exposure
* Validation to prevent a user being both rider and driver in the same trip

---

## Setup

1. Clone the repository:

```bash
git clone <YOUR_REPO_URL>
cd safe_boda
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

* Windows: `.\.venv\Scripts\activate`
* macOS/Linux: `source .venv/bin/activate`

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Run the server:

```bash
python manage.py runserver
```

---

## Models

### CustomUser

* Inherits from Django's `AbstractUser`
* Fields:

  * `username`
  * `email`
  * `password`
  * `user_type` (Rider / Driver)

### Trip

* Fields:

  * `rider` (FK to `CustomUser`)
  * `driver` (FK to `CustomUser`, nullable)
  * `pickup_location` (string)
  * `dropoff_location` (string)
  * `status` (REQUESTED / IN_PROGRESS / COMPLETED)
  * `created_at` (timestamp)

---

## Serializers

* **UserSerializer**

  * Handles serialization/deserialization for `CustomUser`
  * Password is write-only
  * Creates users using `create_user` for hashed passwords

* **TripSerializer**

  * Handles serialization/deserialization for `Trip`
  * Validates that rider and driver are not the same

---

## Views

* **UserViewSet**

  * Full CRUD operations for users
  * Endpoint: `/api/users/`

* **TripViewSet**

  * Full CRUD operations for trips
  * Endpoint: `/api/trips/`

---

## URLs / Endpoints

| Method | Endpoint           | Description                  |
| ------ | ------------------ | ---------------------------- |
| GET    | `/api/users/`      | List all users               |
| POST   | `/api/users/`      | Create a new user            |
| GET    | `/api/users/<id>/` | Retrieve a specific user     |
| PATCH  | `/api/users/<id>/` | Update a specific user       |
| DELETE | `/api/users/<id>/` | Delete a specific user       |
| GET    | `/api/trips/`      | List all trips               |
| POST   | `/api/trips/`      | Create a new trip            |
| GET    | `/api/trips/<id>/` | Retrieve a specific trip     |
| PATCH  | `/api/trips/<id>/` | Update a trip (e.g., status) |
| DELETE | `/api/trips/<id>/` | Delete a specific trip       |

---

## Testing with Postman

1. Open Postman and set the request URL to your local server, e.g., `http://127.0.0.1:8000/api/users/`
2. Test **User Endpoints**:

   * Create user: POST JSON

```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "securepassword",
  "user_type": "Rider"
}
```

* List users: GET `/api/users/`

3. Test **Trip Endpoints**:

   * Create trip: POST JSON

```json
{
  "rider": 1,
  "driver": 2,
  "pickup_location": "Kigali",
  "dropoff_location": "Gisozi",
  "status": "REQUESTED"
}
```

* Update status: PATCH `/api/trips/1/` with `{ "status": "IN_PROGRESS" }`
* Delete trip: DELETE `/api/trips/1/`

---

## Security & Validation

* Passwords are write-only in serializers
* Users cannot be both rider and driver in the same trip
* Status field has restricted choices (`REQUESTED`, `IN_PROGRESS`, `COMPLETED`)

---

