document.addEventListener("DOMContentLoaded", function() {
    // Get all product buttons
    var productButtons = document.querySelectorAll('.product-button');

    // Add click event listener to each button
    productButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            var productId = this.getAttribute('data-product-id');
            var modal = document.getElementById('modal-' + productId);
            modal.style.display = 'block';
        });
    });

    // Get all close buttons
    var closeButtons = document.querySelectorAll('.close-product-details');

    // Add click event listener to each close button
    closeButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            var modal = this.parentElement;
            modal.style.display = 'none';
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var modal = document.getElementById("custom-modal");
    var closeModalBtn = modal.querySelector(".close");
    var confirmDeleteBtn = modal.querySelector("#confirm-delete");
    var cancelDeleteBtn = modal.querySelector("#cancel-delete");

    // Get all delete buttons in the wishlist
    var deleteButtons = document.querySelectorAll(".delete-button");

    // Variable to hold the form associated with the delete action
    var deleteForm = null;

    // Loop through each delete button and attach event listeners
    deleteButtons.forEach(function(deleteButton) {
        deleteButton.addEventListener("click", function(event) {
            event.preventDefault();
            modal.style.display = "block";
            
            // Get the associated form for the current delete button
            deleteForm = deleteButton.closest('form');

            // Event listener for confirmation button
            confirmDeleteBtn.onclick = function() {
                deleteForm.submit(); // Submit the delete form
                modal.style.display = "none"; // Hide the modal after submission
            };
        });
    });

    closeModalBtn.addEventListener("click", function(event) {
        event.preventDefault();
        modal.style.display = "none";
    });

    cancelDeleteBtn.addEventListener("click", function(event) {
        event.preventDefault();
        modal.style.display = "none";
    });
});

console.log('product.js has loaded')
