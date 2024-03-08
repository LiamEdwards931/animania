function moveLinks(){
    let container = document.getElementById('linksContainer');
    container.classList.remove('ms-auto');
}

// banner image js-------------------------------------------------------------------
var images = document.querySelectorAll('.img-banner');

document.querySelector('.banner-container').addEventListener('click', function() {
    // function that allows users to click the image to move to the next one in the list
    var visibleImage = document.querySelector('.img-banner.banner-visible');
    var visibleIndex = Array.from(images).indexOf(visibleImage);
    var nextIndex = (visibleIndex + 1) % images.length;
    var nextImage = images[nextIndex];
    
    visibleImage.classList.remove('banner-visible');
    visibleImage.classList.add('banner-hidden');
    nextImage.classList.remove('banner-hidden');
    nextImage.classList.add('banner-visible');
});

// circle indicators
var images = document.querySelectorAll('.img-banner');
var indicator = document.querySelector('.indicator');

images.forEach(function(image, index) {
    // Appends a new circle indicator for each new image that is added to the banner screen
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

document.addEventListener("DOMContentLoaded", function() {
    // Creates dynamic buttons for each of the images, changes text and urls based on the image displayed.
    var images = document.querySelectorAll('.img-banner');
    var shopButton = document.querySelector('.shop-btn');
  
    var buttonSettings = [
        { text: 'Shop Sword Art Online Merch', url: '/shop-now-page' }, 
        { text: 'Shop Demon Slayer Merch', url: '/shop-demon-slayer-page' }, 
        { text: 'Shop Tokyo Ghoul Merch', url: '/shop-tokyo-ghoul-page' } 
    ];

    function updateButtonSettings(index) {
        shopButton.textContent = buttonSettings[index].text;
        shopButton.setAttribute('onclick', `window.location.href='${buttonSettings[index].url}'`);
    }

    document.querySelector('.banner-container').addEventListener('click', function() {
        
        var visibleImage = document.querySelector('.img-banner.banner-visible');
        
        
        var visibleIndex = Array.from(images).indexOf(visibleImage);
        
        
        updateButtonSettings(visibleIndex);
    });
});

function toggle_read() {
    let readmore = document.querySelector('.readmore');
    let toggle = document.querySelector('.readmore-toggle');

    if (readmore.classList.contains('active')) {
        readmore.classList.remove('active');
        toggle.textContent = 'Read more..';
    } else {
        readmore.classList.add('active');
        toggle.textContent = 'Show less..';
    }
}

