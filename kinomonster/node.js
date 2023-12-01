let isLightMode = true;

function toggleMode() {
    const body = document.body;
    const toggleButton = document.getElementById("toggleButton");

    if (isLightMode) {
        body.classList.remove("light-mode");
        body.classList.add("dark-mode");
        toggleButton.innerHTML = "\uD83D\uDE01"; // Change to a different smiley
    } else {
        body.classList.remove("dark-mode");
        body.classList.add("light-mode");
        toggleButton.innerHTML = "\uD83D\uDE00"; // Change back to the original smiley
    }

    // Toggle the mode flag
    isLightMode = !isLightMode;
}