// banner image js-------------------------------------------------------------------
var images = document.querySelectorAll('.img-banner');

document.querySelector('.banner-container').addEventListener('click', function() {
    var visibleImage = document.querySelector('.img-banner.banner-visible');
    var visibleIndex = Array.from(images).indexOf(visibleImage);
    var nextIndex = (visibleIndex + 1) % images.length;
    var nextImage = images[nextIndex];
    
    visibleImage.classList.remove('banner-visible');
    visibleImage.classList.add('banner-hidden');
    nextImage.classList.remove('banner-hidden');
    nextImage.classList.add('banner-visible');
});


var images = document.querySelectorAll('.img-banner');
var indicator = document.querySelector('.indicator');

// circle indicators
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

