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
