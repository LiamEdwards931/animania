// // Timesout the message container after 5 seconds of appearing
const messageContainer = document.getElementById('remove-message');

    setTimeout(() => {
        if (messageContainer) {
            messageContainer.remove();
        }
    }, 5000);