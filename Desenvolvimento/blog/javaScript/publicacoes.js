// Função para mostrar as publicações salvas
function mostrarPublicacoes() {
    // Obtém as publicações salvas do armazenamento local ou inicializa um array vazio se não houver publicações
    var publicacoesSalvas = JSON.parse(localStorage.getItem("publicacoes")) || [];
    // Obtém a referência para a div onde as publicações serão exibidas
    var conteudoDiv = document.getElementById("conteudo");

    // Verifica se há publicações salvas
    if (publicacoesSalvas.length === 0) {
        // Se não houver publicações, exibe uma mensagem indicando que não há publicações disponíveis
        conteudoDiv.innerHTML = "<h3 class='no-posts'>Nenhuma publicação disponível.</h3>";
    } else {
        // Se houver publicações salvas, limpa o conteúdo atual da div
        conteudoDiv.innerHTML = ""; // Limpa o conteúdo atual
        // Itera sobre cada publicação salva
        publicacoesSalvas.forEach(function (publicacao) {
            // Cria um elemento div para representar a publicação
            var div = document.createElement("div");
            div.className = "card";

            // Cria um elemento de âncora para o link da publicação
            var a = document.createElement("a");
            a.className = "card-link";
            a.href = "detalhes_publicacao.html"; // Define o link para a página de detalhes da publicação
            // Define o conteúdo HTML do link com base nas informações da publicação
            a.innerHTML = `
                <h2>${publicacao.titulo}</h2>
                <p>${publicacao.descricao}</p>
                <img src="${publicacao.imagem}" alt="Imagem">
            `;
            // Adiciona o elemento de âncora à div da publicação
            div.appendChild(a);

            // Adiciona a div da publicação à div de conteúdo
            conteudoDiv.appendChild(div);
        });
    }
}

// Evento onload é acionado quando a página é completamente carregada
window.onload = function () {
    // Chama a função para mostrar as publicações salvas quando a página é carregada
    mostrarPublicacoes();
};

// Função para exibir um pop-up com uma mensagem
function showPopup(message, activated) {
    const popup = document.getElementById('popup');
    popup.textContent = message;
    popup.style.display = 'block';
    setTimeout(() => {
        popup.style.display = 'none';
    }, 3000); // Remove o pop-up após 3 segundos
}

// Seleção dos elementos do HTML que serão manipulados
const toggleDarkModeLink = document.getElementById("toggleDarkMode");
const toggleColorBlindModeLink = document.getElementById("toggleColorBlindMode");
const increaseFontSizeLink = document.getElementById("increaseFontSize");
const decreaseFontSizeLink = document.getElementById("decreaseFontSize");
const body = document.body;

// Event listener para o botão "Modo Escuro"
toggleDarkModeLink.addEventListener("click", function () {
    // Alternar a classe 'dark-mode' no elemento body
    body.classList.toggle("dark-mode");
    // Alternar a classe 'dark-mode-active' no botão 'Modo Escuro'
    toggleDarkModeLink.classList.toggle("dark-mode-active");
    // Exibir pop-up informando o estado atual do modo escuro
    showPopup(body.classList.contains("dark-mode") ? "Modo Escuro ativado" : "Modo Escuro desativado", body.classList.contains("dark-mode"));
});

// Event listener para o botão "Modo Daltonismo"
toggleColorBlindModeLink.addEventListener("click", function () {
    // Alternar a classe 'color-blind-mode' no elemento body
    body.classList.toggle("color-blind-mode");
    // Alternar a classe 'color-blind-mode-active' no botão 'Modo Daltonismo'
    toggleColorBlindModeLink.classList.toggle("color-blind-mode-active");
    // Exibir pop-up informando o estado atual do modo daltonismo
    showPopup(body.classList.contains("color-blind-mode") ? "Modo Daltonismo ativado" : "Modo Daltonismo desativado", body.classList.contains("color-blind-mode"));
});

// Event listener para o botão "Aumentar Fonte"
increaseFontSizeLink.addEventListener("click", function () {
    // Obter o tamanho atual da fonte
    const currentFontSize = parseFloat(window.getComputedStyle(document.body, null).getPropertyValue('font-size'));
    // Aumentar o tamanho da fonte em 1 pixel
    document.body.style.fontSize = (currentFontSize + 1) + 'px';
    // Exibir pop-up informando que a fonte foi aumentada
    showPopup("Fonte aumentada", true);
});

// Event listener para o botão "Diminuir Fonte"
decreaseFontSizeLink.addEventListener("click", function () {
    // Obter o tamanho atual da fonte
    const currentFontSize = parseFloat(window.getComputedStyle(document.body, null).getPropertyValue('font-size'));
    // Diminuir o tamanho da fonte em 1 pixel
    document.body.style.fontSize = (currentFontSize - 1) + 'px';
    // Exibir pop-up informando que a fonte foi diminuída
    showPopup("Fonte diminuída", true);
});