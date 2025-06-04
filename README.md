# LibbyGraph-Sync

An app built to sync my to-read pile between StoryGraph and Libby.

## Overview

users upload their exported StoryGraph data and the app recommends which books to place holds on next from Libby. It uses:

- **Backend**: FastAPI with PostgreSQL database
- **Frontend**: React with TypeScript

## Setup Instructions

### Prerequisites

- [Python 3.9+](https://www.python.org/downloads/)
- [Node.js and npm](https://nodejs.org/)
- [PostgreSQL](https://www.postgresql.org/download/)

### PostgreSQL Setup

1. Install PostgreSQL from the [official website](https://www.postgresql.org/download/windows/)
2. During installation, note the password you set for the "postgres" user
3. Remember the port number (default is 5432)
4. After installation, create a database named "libgraph"
   - Using pgAdmin: Right-click on "Databases" → Create → Database → Enter "libgraph"

### Backend Setup

1. Clone the repo
   ```
   git clone <repository-url>
   cd LibbyGraph-Sync
   ```

2. Set up a Python virtual environment
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install fastapi uvicorn pandas python-multipart sqlalchemy psycopg2-binary alembic python-dotenv
   ```

4. Configure the database connection
   - Open `backend/database.py`
   - Ensure the `DATABASE_URL` has your correct PostgreSQL username, password, and port
   - Example: `postgresql://postgres:your_password@localhost:5432/libgraph`

5. Initialize the database
   ```
   cd backend
   python init_db.py
   ```

6. Run the FastAPI server
   ```
   uvicorn main:app --reload
   ```

7. The API will be available at http://127.0.0.1:8000
   - Swagger UI documentation: http://127.0.0.1:8000/docs

### Frontend Setup

1. Navigate to the frontend directory
   ```
   cd frontend
   ```

2. Install dependencies
   ```
   npm install
   ```

3. Start the development server
   ```
   npm run dev
   ```

4. The React application will be available at http://localhost:5173

## API Endpoints

- `GET /`: Welcome message
- `GET /library/upload/`: Library summary API welcome message
- `POST /library/upload/`: Upload a CSV file with book data
- `GET /library/books/`: Get all books from the database

## Development

- Backend code is in the `backend` directory
- Frontend code is in the `frontend/src` directory
- Database models are defined in `backend/db_models.py`
- API endpoints are defined in `backend/post_library_summary.py`