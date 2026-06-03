from flask import Flask, render_template, request, redirect, url_for, flash
from db import db
from models import Student

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "replace-with-a-secure-secret"

# Initialize SQLAlchemy with Flask app
db.init_app(app)

with app.app_context():
    # Create the database file and tables automatically if they do not exist
    db.create_all()


@app.route("/", methods=["GET"])
def index():
    """Display the homepage with the list of all students."""
    students = Student.query.order_by(Student.id).all()
    return render_template("index.html", students=students)


@app.route("/add", methods=["POST"])
def add_student():
    """Create a new student record in the database."""
    name = request.form.get("name", "").strip()
    age = request.form.get("age", "").strip()

    # Server-side validation for safety and integrity
    if not name:
        flash("Please enter a student name.", "error")
        return redirect(url_for("index"))

    try:
        age_value = int(age)
    except ValueError:
        flash("Please enter a valid age between 1 and 120.", "error")
        return redirect(url_for("index"))

    if age_value < 1 or age_value > 120:
        flash("Age must be between 1 and 120.", "error")
        return redirect(url_for("index"))

    new_student = Student(name=name, age=age_value)
    db.session.add(new_student)
    db.session.commit()

    flash("Student added successfully.", "success")
    return redirect(url_for("index"))


@app.route("/update/<int:id>", methods=["POST"])
def update_student(id):
    """Update an existing student record."""
    student = Student.query.get_or_404(id)
    name = request.form.get("name", "").strip()
    age = request.form.get("age", "").strip()

    if not name:
        flash("Please enter a student name.", "error")
        return redirect(url_for("index"))

    try:
        age_value = int(age)
    except ValueError:
        flash("Please enter a valid age between 1 and 120.", "error")
        return redirect(url_for("index"))

    if age_value < 1 or age_value > 120:
        flash("Age must be between 1 and 120.", "error")
        return redirect(url_for("index"))

    student.name = name
    student.age = age_value
    db.session.commit()

    flash("Student updated successfully.", "success")
    return redirect(url_for("index"))


@app.route("/delete/<int:id>", methods=["POST"])
def delete_student(id):
    """Delete a student record from the database."""
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()

    flash("Student deleted successfully.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
