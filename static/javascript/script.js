// --------------------------Base.html script----------------------------------------------------------------

// Moves the links to the bottom left of the dropdown bar when the navbar dropdown button is clicked
function moveLinks(){
    let container = document.getElementById('linksContainer');
    container.classList.remove('ms-auto');
};

function toggle_read() {
    // Opens the dropdown on the footer to allow users to read more about the site.
    let readmore = document.querySelector('.readmore');
    let toggle = document.querySelector('.readmore-toggle');

    if (readmore.classList.contains('active')) {
        readmore.classList.remove('active');
        toggle.textContent = 'Read more..';
    } else {
        readmore.classList.add('active');
        toggle.textContent = 'Show less..';
    }
};

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