document.addEventListener("DOMContentLoaded", function () {
    const invalid = document.querySelectorAll(".form-control.is-invalid");
    invalid.forEach((input) => {
        input.addEventListener("input", function() {
            input.classList.remove("is-invalid");
        });
    });
});