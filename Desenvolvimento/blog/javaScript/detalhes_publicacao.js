function showPopup(message, activated) {
    const popup = document.getElementById('popup');
    popup.textContent = message;
    popup.style.display = 'block';
    setTimeout(() => {
        popup.style.display = 'none';
    }, 3000);
}

const toggleDarkModeLink = document.getElementById("toggleDarkMode");
const toggleColorBlindModeLink = document.getElementById("toggleColorBlindMode");
const increaseFontSizeLink = document.getElementById("increaseFontSize");
const decreaseFontSizeLink = document.getElementById("decreaseFontSize");
const body = document.body;

toggleDarkModeLink.addEventListener("click", function () {
    body.classList.toggle("dark-mode");
    toggleDarkModeLink.classList.toggle("dark-mode-active");
    showPopup(body.classList.contains("dark-mode") ? "Modo Escuro ativado" : "Modo Escuro desativado", body.classList.contains("dark-mode"));
});

toggleColorBlindModeLink.addEventListener("click", function () {
    body.classList.toggle("color-blind-mode");
    toggleColorBlindModeLink.classList.toggle("color-blind-mode-active");
    showPopup(body.classList.contains("color-blind-mode") ? "Modo Daltonismo ativado" : "Modo Daltonismo desativado", body.classList.contains("color-blind-mode"));
});

increaseFontSizeLink.addEventListener("click", function () {
    const currentFontSize = parseFloat(window.getComputedStyle(document.body, null).getPropertyValue('font-size'));
    document.body.style.fontSize = (currentFontSize + 1) + 'px';
    showPopup("Fonte aumentada", true);
});

decreaseFontSizeLink.addEventListener("click", function () {
    const currentFontSize = parseFloat(window.getComputedStyle(document.body, null).getPropertyValue('font-size'));
    document.body.style.fontSize = (currentFontSize - 1) + 'px';
    showPopup("Fonte diminuída", true);
});
