# Personal Growth Tracker

A full-stack application built using **FastAPI** and **React** to track personal growth habits with secure user authentication.

---

## 🚀 Features

- **User Registration & Login** (with JWT Authentication)
- **Habit Management**:
  - Create new habits
  - View all habits
  - Update existing habits
  - Delete habits
- **Authentication-protected endpoints** (only logged-in users can manage their habits)
- **Clean modular structure** (organized routes, schemas, utils)
- **Fully documented API using FastAPI's interactive `/docs` (Swagger UI)**

---

## 🖥️ Frontend (React)

A lightweight React-based UI to interact with the backend features.

### Features

- User Registration and Login
- Token-based protected dashboard
- Axios-based API communication
- React Router for navigation
- Minimal CSS styling (customizable for production)

### Tech Stack

- **React 18**
- **React Router DOM**
- **Axios**
- **JavaScript (ES6+)**

### Setup Instructions

1. **Navigate to the frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Run the frontend**
   ```bash
   npm start
   ```

4. **Access the App**
   [http://localhost:3000](http://localhost:3000)

---

## 🔐 Frontend Authentication Flow

- On login, JWT token is saved in `localStorage`
- Dashboard fetches protected data using the token in `Authorization` header
- Logout removes the token and redirects to the login screen

---

## 🧠 Backend (FastAPI)

Backend REST API built using FastAPI with JWT-based authentication.

### Tech Stack

- **Python 3.11**
- **FastAPI**
- **Uvicorn** (development server)
- **Pydantic** (data validation)
- **passlib** (for password hashing)
- **JWT** (JSON Web Tokens for authentication)

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/Swap98/personal-growth-tracker-api.git
cd personal-growth-tracker-api
```

2. **Create a virtual environment and activate it**

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the server**

```bash
uvicorn main:app --reload
```

5. **Access the API docs**

Visit:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔐 Authentication

- Register a user at `/users/register`
- Log in at `/users/login` to receive an access token
- Authorize your requests using the token in `/docs` (Authorize button)

---

## 📄 License

This project is currently personal and private.

---
