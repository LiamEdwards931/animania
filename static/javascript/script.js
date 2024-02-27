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


// dynamic button------------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function() {
    // Get references to elements
    var images = document.querySelectorAll('.img-banner');
    var shopButton = document.querySelector('.shop-btn');

    // Define text and URL mappings for each image
    var buttonSettings = [
        { text: 'Shop Sword Art Online', url: '/shop-now-page' }, // For sword art online image
        { text: 'Shop Demon Slayer', url: '/shop-demon-slayer-page' }, // For demon slayer image
        { text: 'Shop Tokyo Ghoul', url: '/shop-tokyo-ghoul-page' } // For tokyo ghoul image
    ];

    // Function to update button text and URL based on currently displayed image
    function updateButtonSettings(index) {
        shopButton.textContent = buttonSettings[index].text;
        shopButton.setAttribute('onclick', `window.location.href='${buttonSettings[index].url}'`);
    }

    // Add event listener to the banner container
    document.querySelector('.banner-container').addEventListener('click', function() {
        // Find the currently visible image
        var visibleImage = document.querySelector('.img-banner.banner-visible');
        
        // Find the index of the currently visible image
        var visibleIndex = Array.from(images).indexOf(visibleImage);
        
        // Update button text and URL based on the currently displayed image
        updateButtonSettings(visibleIndex);
    });
});


