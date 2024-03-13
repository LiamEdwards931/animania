document.getElementById('all-product-details').addEventListener('click', function() {
    let content = document.getElementById('all-details-container');
    content.style.display = 'block';
});

document.getElementById('close-product-details').addEventListener('click', function() {
    let content = document.getElementById('all-details-container');
    content.style.display = 'none';
});
