function publicar() {
    var titulo = document.getElementById("titulo").value.trim();
    var descricao = document.getElementById("descricao").value.trim();
    var imagem = document.getElementById("imagem").files[0];

    if (titulo && descricao && imagem) {
        var reader = new FileReader();
        reader.onload = function (event) {
            var imagemURL = event.target.result;
            var publicacao = {
                titulo: titulo,
                descricao: descricao,
                imagem: imagemURL
            };

            var publicacoesSalvas = JSON.parse(localStorage.getItem("publicacoes")) || [];
            publicacoesSalvas.push(publicacao);
            localStorage.setItem("publicacoes", JSON.stringify(publicacoesSalvas));

            alert("Publicação realizada com sucesso!");
            limparFormulario();
        };
        reader.readAsDataURL(imagem);
    } else {
        alert("Por favor, preencha todos os campos obrigatórios.");
    }
}

function limparLocalStorage() {
    localStorage.removeItem("publicacoes");
    location.reload();
}

function limparFormulario() {
    document.getElementById("titulo").value = "";
    document.getElementById("descricao").value = "";
    document.getElementById("imagem").value = "";
}

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
