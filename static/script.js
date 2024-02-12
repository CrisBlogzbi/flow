// Execute the code when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Select all comment forms, add-comment forms, and reply forms
    var commentForms = document.querySelectorAll(".comment-form, .add-comment-form, .reply-form");

    // Add a click event listener to the document body
    document.body.addEventListener("click", function (event) {
        // Find the closest ancestor element with the class "add-comment-button"
        var button = event.target.closest(".add-comment-button");
        
        // Check if the button exists
        if (button) {
            // Get the data-comment-id attribute value from the button
            var commentId = button.getAttribute("data-comment-id");
            
            // Construct the form selector based on the data-comment-id
            var formSelector = commentId === "add" ? ".add-comment-form" : ".comment-form[data-comment-id='" + commentId + "']";
            
            // Find the form element using the constructed selector
            var form = document.querySelector(formSelector);

            // Check if the form exists
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
                // Log an error if the form is not found
                console.error("Form not found for Comment ID:", commentId);
            }
        }
    });

    // Find the delete post button
    var deletePostButton = document.querySelector(".delete-post-button");

    // Add a click event listener to the delete post button
    if (deletePostButton) {
        deletePostButton.addEventListener("click", function (event) {
            // Display a confirmation dialog before allowing the action
            if (!confirm("Are you sure you want to delete this post?")) {
                // Prevent the default action if the user cancels the confirmation
                event.stopImmediatePropagation();
                event.preventDefault();
            }
        });
    }
});
