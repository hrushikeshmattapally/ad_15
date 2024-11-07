function toggleSettingsMenu() {
    const settingsMenu = document.getElementById('settingsMenu');
    settingsMenu.style.display = settingsMenu.style.display === 'block' ? 'none' : 'block';
}

// Close the menu when clicking outside
document.addEventListener('click', function(event) {
    const settingsMenu = document.getElementById('settingsMenu');
    const settingsIcon = document.querySelector('.settings-icon');

    if (!settingsMenu.contains(event.target) && !settingsIcon.contains(event.target)) {
        settingsMenu.style.display = 'none';
    }
});
