// Função para realizar a publicação
function publicar() {
    // Obtém os valores dos campos de título, descrição e imagem do formulário e remove espaços em branco extras
    var titulo = document.getElementById("titulo").value.trim();
    var descricao = document.getElementById("descricao").value.trim();
    var imagem = document.getElementById("imagem").files[0]; // Arquivo de imagem

    // Verifica se todos os campos obrigatórios estão preenchidos
    if (titulo && descricao && imagem) {
        // Se os campos estiverem preenchidos, cria um novo FileReader para ler a imagem
        var reader = new FileReader();
        reader.onload = function (event) {
            // Quando a imagem é carregada com sucesso, obtém a URL da imagem convertida
            var imagemURL = event.target.result; // URL da imagem convertida
            // Cria um objeto contendo os dados da publicação
            var publicacao = {
                titulo: titulo,
                descricao: descricao,
                imagem: imagemURL
            };

            // Obtém as publicações salvas do armazenamento local ou inicializa um array vazio se não houver publicações
            var publicacoesSalvas = JSON.parse(localStorage.getItem("publicacoes")) || [];
            // Adiciona a nova publicação ao array de publicações
            publicacoesSalvas.push(publicacao);
            // Atualiza as publicações salvas no armazenamento local
            localStorage.setItem("publicacoes", JSON.stringify(publicacoesSalvas));

            // Exibe um alerta informando que a publicação foi realizada com sucesso
            alert("Publicação realizada com sucesso!");
            // Limpa o formulário após a publicação ser realizada com sucesso
            limparFormulario();
        };
        // Converte a imagem em Data URL
        reader.readAsDataURL(imagem);
    } else {
        // Se algum campo obrigatório estiver em branco, exibe um alerta solicitando que todos os campos sejam preenchidos
        alert("Por favor, preencha todos os campos obrigatórios.");
    }
}

// Função para limpar todas as publicações do armazenamento local e recarregar a página
function limparLocalStorage() {
    localStorage.removeItem("publicacoes"); // Remove todas as publicações do armazenamento local
    location.reload(); // Recarrega a página para refletir as alterações
}

// Função para limpar o formulário de publicação
function limparFormulario() {
    // Limpa os valores dos campos de título, descrição e imagem do formulário
    document.getElementById("titulo").value = "";
    document.getElementById("descricao").value = "";
    document.getElementById("imagem").value = "";
}

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