from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy ORM instance
# This object will be shared between the Flask app and the models.
db = SQLAlchemy()
