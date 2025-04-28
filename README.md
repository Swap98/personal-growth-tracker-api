# Personal Growth Tracker API

A backend REST API built using **FastAPI** to track personal growth habits with secure user authentication.

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

## 📚 Tech Stack

- **Python 3.11**
- **FastAPI**
- **Uvicorn** (development server)
- **Pydantic** (data validation)
- **passlib** (for password hashing)
- **JWT** (JSON Web Tokens for authentication)

---

## 🛠 Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/Swap98/personal-growth-tracker-api.git
   cd personal-growth-tracker-api
   ```

2. **Create a virtual environment and activate it**

   ```bash
   python -m venv venv
   ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On Mac/Linux:

     ```bash
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

   Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔐 Authentication

- Register a user at `/users/`
- Log in at `/users/login` to receive an access token
- Authorize your requests using the token inside `/docs` (Authorize button)

---

## 📈 Future Improvements

- Add Expense Tracking Module
- Add Habit Completion Tracking (habit streaks)
- Deploy to Render / AWS / Railway

---

## 📄 License

This project is currently personal and private.
