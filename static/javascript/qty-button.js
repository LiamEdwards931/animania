// script to submit the form and increment or decrement the quantity
console.log('hello')
document.addEventListener('DOMContentLoaded', function() {
    const minusButtons = document.querySelectorAll('.quantity-btn.minus');
    const plusButtons = document.querySelectorAll('.quantity-btn.plus');
    const quantityInputs = document.querySelectorAll('.quantity');

    minusButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            event.preventDefault();
            const index = Array.from(minusButtons).indexOf(button);
            let value = parseInt(quantityInputs[index].value);
            if (!isNaN(value) && value > 1) {
                quantityInputs[index].value = value - 1;
                // Trigger form submission
                quantityInputs[index].closest('form').submit();
            }
        });
    });

    plusButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            event.preventDefault();
            const index = Array.from(plusButtons).indexOf(button);
            let value = parseInt(quantityInputs[index].value);
            if (!isNaN(value)) {
                quantityInputs[index].value = value + 1;
                // Trigger form submission
                quantityInputs[index].closest('form').submit();
            }
        });
    });
});
