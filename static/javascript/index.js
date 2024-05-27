// ---------------------Index.html script------------------
// banner image js function that allows users to click the image to move to the next one in the list
var images = document.querySelectorAll('.img-banner');
var imageButton = document.querySelectorAll('.banner-form-button');

document.querySelector('.banner-container').addEventListener('click', function() {
    var visibleImage = document.querySelector('.img-banner.banner-visible');
    var visibleForm = document.querySelector('.banner-form-button.form-visible');
    var visibleIndex = Array.from(images).indexOf(visibleImage);
    var VisibleButtonIndex = Array.from(imageButton).indexOf(visibleForm);
    var nextIndex = (visibleIndex + 1) % images.length;
    var nextButtonIndex = (VisibleButtonIndex + 1) % imageButton.length;
    var nextImage = images[nextIndex];
    var nextButton = imageButton[nextButtonIndex];
    
    visibleImage.classList.remove('banner-visible');
    visibleImage.classList.add('banner-hidden');
    nextImage.classList.remove('banner-hidden');
    nextImage.classList.add('banner-visible');
    visibleForm.classList.remove('form-visible');
    visibleForm.classList.add('form-hidden');
    nextButton.classList.remove('form-hidden');
    nextButton.classList.add('form-visible');
});

// circle indicators for the image banners
var images = document.querySelectorAll('.img-banner');
var indicator = document.querySelector('.indicator');

// Appends a new circle indicator for each new image that is added to the banner screen
images.forEach(function(image, index) {
    var circle = document.createElement('div');
    circle.classList.add('indicator-circle');
    if (index === 0) {
        circle.classList.add('active');
    }
    indicator.appendChild(circle);
});

// Fills circles depending on the image you are on
document.querySelector('.banner-container').addEventListener('click', function() {
    var visibleImage = document.querySelector('.img-banner.banner-visible');
    var visibleIndex = Array.from(images).indexOf(visibleImage);
    
    var circles = document.querySelectorAll('.indicator-circle');
    circles.forEach(function(circle, index) {
        if (index === visibleIndex) {
            circle.classList.add('active'); 
        } else {
            circle.classList.remove('active');
        }
    });
});

function removeDelivery(){
    let delivery_container = document.getElementById('delivery-container');

    delivery_container.style.display = 'none';
}