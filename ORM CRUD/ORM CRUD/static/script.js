const studentForm = document.getElementById("student-form");
const nameInput = document.getElementById("name");
const ageInput = document.getElementById("age");
const submitBtn = document.getElementById("submit-btn");
const cancelBtn = document.getElementById("cancel-btn");
const nameError = document.getElementById("name-error");
const ageError = document.getElementById("age-error");
let editingId = null;

function clearValidation() {
    nameError.textContent = "";
    ageError.textContent = "";
}

function resetForm() {
    editingId = null;
    studentForm.action = "/add";
    submitBtn.textContent = "Add Student";
    submitBtn.classList.remove("btn-update");
    submitBtn.classList.add("btn-add");
    cancelBtn.classList.add("hidden");
    nameInput.value = "";
    ageInput.value = "";
    clearValidation();
}

function validateForm() {
    let valid = true;
    clearValidation();

    const nameValue = nameInput.value.trim();
    const ageValue = ageInput.value.trim();
    const ageNumber = Number(ageValue);

    if (!nameValue) {
        nameError.textContent = "Student name cannot be empty.";
        valid = false;
    }

    if (!ageValue || Number.isNaN(ageNumber)) {
        ageError.textContent = "Please enter a valid age.";
        valid = false;
    } else if (ageNumber < 1 || ageNumber > 120) {
        ageError.textContent = "Age must be between 1 and 120.";
        valid = false;
    }

    return valid;
}

studentForm.addEventListener("submit", (event) => {
    if (!validateForm()) {
        event.preventDefault();
    }
});

cancelBtn.addEventListener("click", resetForm);

const editButtons = document.querySelectorAll(".btn-edit");
editButtons.forEach((button) => {
    button.addEventListener("click", () => {
        editingId = button.dataset.id;
        const studentName = button.dataset.name;
        const studentAge = button.dataset.age;

        nameInput.value = studentName;
        ageInput.value = studentAge;
        studentForm.action = `/update/${editingId}`;
        submitBtn.textContent = "Update Student";
        submitBtn.classList.remove("btn-add");
        submitBtn.classList.add("btn-update");
        cancelBtn.classList.remove("hidden");
        nameInput.focus();
    });
});

const deleteForms = document.querySelectorAll(".delete-form");
deleteForms.forEach((form) => {
    form.addEventListener("submit", (event) => {
        const confirmed = window.confirm("Are you sure you want to delete this student?");
        if (!confirmed) {
            event.preventDefault();
        }
    });
});

// Reset the form after page load so accidental edits don't persist across refreshes.
window.addEventListener("load", resetForm);
