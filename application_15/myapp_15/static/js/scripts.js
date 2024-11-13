document.addEventListener("DOMContentLoaded", function() {
    const darkThemeNotification = document.querySelector(".dark-theme");
    const gotItButton = darkThemeNotification.querySelector("button");
    const turnOnButton = darkThemeNotification.querySelector(".turn-on");

    // Hide the notification when "Got it" is clicked
    gotItButton.addEventListener("click", function() {
        darkThemeNotification.style.display = "none";
    });

    // Toggle dark theme on "Turn it on" button click
    turnOnButton.addEventListener("click", function() {
        document.body.classList.toggle("dark-mode");
    });
});