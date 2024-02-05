document.addEventListener("DOMContentLoaded", function () {
    var commentForms = document.querySelectorAll(".comment-form, .add-comment-form, .reply-form");

    document.body.addEventListener("click", function (event) {
        var button = event.target.closest(".add-comment-button");
        if (button) {
            var commentId = button.getAttribute("data-comment-id");
            var formSelector = commentId === "add" ? ".add-comment-form" : ".comment-form[data-comment-id='" + commentId + "']";
            var form = document.querySelector(formSelector);

            if (form) {
                // Toggle the visibility of the target form
                form.style.display = form.style.display === "" || form.style.display === "none" ? "block" : "none";

                // Hide all other comment forms
                commentForms.forEach(function (otherForm) {
                    if (otherForm !== form) {
                        otherForm.style.display = "none";
                    }
                });
            } else {
                console.error("Form not found for Comment ID:", commentId);
            }
        }
    });
});
