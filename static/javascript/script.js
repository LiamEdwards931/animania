// --------------------------Base.html script----------------------------------------------------------------

// Moves the links to the bottom left of the dropdown bar when the navbar dropdown button is clicked
function moveLinks(){
    let container = document.getElementById('linksContainer');
    container.classList.remove('ms-auto');
}

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
}

