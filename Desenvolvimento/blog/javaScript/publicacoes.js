function mostrarPublicacoes() {
    var publicacoesSalvas = JSON.parse(localStorage.getItem("publicacoes")) || [];
    var conteudoDiv = document.getElementById("conteudo");

    if (publicacoesSalvas.length === 0) {
        conteudoDiv.innerHTML = "<p class='no-posts'>Nenhuma publicação disponível.</p>";
    } else {
        conteudoDiv.innerHTML = "";
        publicacoesSalvas.forEach(function (publicacao) {
            var div = document.createElement("div");
            div.className = "card";

            var a = document.createElement("a");
            a.className = "card-link";
            a.href = "detalhes_publicacao.html";
            a.innerHTML = `
                <h2>${publicacao.titulo}</h2>
                <p>${publicacao.descricao}</p>
                <img src="${publicacao.imagem}" alt="Imagem">
            `;
            div.appendChild(a);

            conteudoDiv.appendChild(div);
        });
    }
}

window.onload = function () {
    mostrarPublicacoes();
};

function showPopup(message, activated) {
    const popup = document.getElementById('popup');
    popup.textContent = message;
    popup.style.display = 'block';
    setTimeout(() => {
        popup.style.display = 'none';
    }, 3000);
}

const ModoEscuroLink = document.getElementById("ModoEscuro");
const toggleColorBlindModeLink = document.getElementById("toggleColorBlindMode");
const increaseFontSizeLink = document.getElementById("increaseFontSize");
const decreaseFontSizeLink = document.getElementById("decreaseFontSize");
const body = document.body;

ModoEscuroLink.addEventListener("click", function () {
    body.classList.toggle("modoEscuroClass");
    ModoEscuroLink.classList.toggle("modoEscuroClass-active");
    showPopup(body.classList.contains("modoEscuroClass") ? "Modo Escuro ativado" : "Modo Escuro desativado", body.classList.contains("modoEscuroClass"));
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
