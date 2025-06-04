from database import engine, Base
import db_models

def init_db():
    """Create database tables from SQLAlchemy models"""
    print("Started creating db tables")
    Base.metadata.create_all(bind=engine)
    print("db tables created successfully")

if __name__ == "__main__":
    init_db() 