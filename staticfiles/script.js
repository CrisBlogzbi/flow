document.addEventListener("DOMContentLoaded", function () {
    var commentForms = document.querySelectorAll(".comment-form, .add-comment-form, .reply-form");

    commentForms.forEach(function (form) {
        form.style.display = "block"; // Hide all comment forms
    });

    document.body.addEventListener("click", function (event) {
        var button = event.target.closest(".add-comment-button");
        if (button) {
            var commentId = button.getAttribute("data-comment-id");
            var formSelector = commentId === "add" ? ".add-comment-form" : ".comment-form[data-comment-id='" + commentId + "']";
            var form = document.querySelector(formSelector);

            if (form) {
                form.style.display = form.style.display === "none" ? "block" : "none";
            } else {
                console.error("Form not found for Comment ID:", commentId);
            }
        }
    });
});
