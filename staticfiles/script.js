document.addEventListener("DOMContentLoaded", function () {
    var commentButtons = document.querySelectorAll(".add-comment-button");
    var commentForms = document.querySelectorAll(".comment-form");
    var replyForms = document.querySelectorAll(".reply-form");

    commentButtons.forEach(function (button, index) {
        button.addEventListener("click", function () {
            var commentForm = commentForms[index];
            toggleFormVisibility(commentForm);
        });
    });

    var replyButtons = document.querySelectorAll(".reply-button");

    replyButtons.forEach(function (button, index) {
        button.addEventListener("click", function () {
            var replyForm = replyForms[index];
            toggleFormVisibility(replyForm);
        });
    });

    // Initially hide all comment and reply forms
    commentForms.forEach(function (commentForm) {
        commentForm.style.display = "none";
    });

    replyForms.forEach(function (replyForm) {
        replyForm.style.display = "none";
    });

    function toggleFormVisibility(form) {
        form.style.display = form.style.display === "none" ? "block" : "none";
    }
});
