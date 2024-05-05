
// Função para exibir o formulário de login e ocultar o formulário de registro
function showLoginForm() {
    document.getElementById('login-form').style.display = 'block'; // Exibe o formulário de login
    document.getElementById('register-form').style.display = 'none'; // Oculta o formulário de registro
}

// Função para exibir o formulário de registro e ocultar o formulário de login
function showRegisterForm() {
    document.getElementById('register-form').style.display = 'block'; // Exibe o formulário de registro
    document.getElementById('login-form').style.display = 'none'; // Oculta o formulário de login
}

// Função para realizar o login
function login() {
    var username = document.getElementById('login-username').value; // Obtém o valor do campo de nome de usuário do formulário de login
    var password = document.getElementById('login-password').value; // Obtém o valor do campo de senha do formulário de login

    // Obter os dados armazenados localmente
    var storedUsername = localStorage.getItem('username'); // Obtém o nome de usuário armazenado localmente
    var storedPassword = localStorage.getItem('password'); // Obtém a senha armazenada localmente

    // Verificar se os dados inseridos correspondem aos dados armazenados
    if (username === storedUsername && password === storedPassword) {
        alert('Login bem-sucedido!'); // Exibe uma mensagem de sucesso se o login for bem-sucedido
        window.location.href = "../blog/html/publicacoes.html"; // Redireciona para a página principal após o login bem-sucedido
        return false; // Impede o envio do formulário
    } else {
        alert('Usuário ou senha incorretos!'); // Exibe uma mensagem de erro se o login falhar
        return false; // Impede o envio do formulário
    }
}

// Função para registrar um novo usuário
function register() {
    var username = document.getElementById('register-username').value; // Obtém o valor do campo de nome de usuário do formulário de registro
    var email = document.getElementById('register-email').value; // Obtém o valor do campo de e-mail do formulário de registro
    var password = document.getElementById('register-password').value; // Obtém o valor do campo de senha do formulário de registro

    // Armazenar dados do usuário no localStorage
    localStorage.setItem('username', username); // Armazena o nome de usuário localmente
    localStorage.setItem('email', email); // Armazena o e-mail localmente
    localStorage.setItem('password', password); // Armazena a senha localmente

    alert('Cadastro bem-sucedido!'); // Exibe uma mensagem de sucesso após o registro bem-sucedido
    return true; // Permite o envio do formulário
}

