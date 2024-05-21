document.addEventListener("DOMContentLoaded", function () {
    const invalid = document.querySelectorAll(".form-control.is-invalid");

    invalid.forEach((input) => {
        input.addEventListener("input", function() {
            input.classList.remove("is-invalid");
        });
    });

    const email_form = document.querySelector(".email-form")
    const requiredFields = email_form.querySelectorAll('[required]');
    const loading_container = document.querySelector('.loading-container');
    const send_btn = document.querySelector(".send-email")
    send_btn.addEventListener("click", function() {
        let allFieldsFilled = true;

        requiredFields.forEach(function(field) {
            if (!field.value.trim()) {
                allFieldsFilled = false;
            }
        });

        if (allFieldsFilled) {
            loading_container.innerHTML = `
                <div class="d-flex align-items-center loading">
                    <strong role="status">Wysyłanie...</strong>
                    <div class="spinner-border ms-auto" aria-hidden="true"></div>
                </div>`;
        }
    })
});