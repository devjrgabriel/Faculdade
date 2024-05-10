function showLoginForm() {
    document.getElementById('login-form').style.display = 'block';
    document.getElementById('register-form').style.display = 'none';
}

function showRegisterForm() {
    document.getElementById('register-form').style.display = 'block';
    document.getElementById('login-form').style.display = 'none';
}

function login() {
    var username = document.getElementById('login-username').value;
    var password = document.getElementById('login-password').value;

    var storedUsername = localStorage.getItem('username');
    var storedPassword = localStorage.getItem('password');

    if (username === storedUsername && password === storedPassword) {
        alert('Login bem-sucedido!');
        window.location.href = "../blog/html/publicacoes.html";
        return false;
    } else {
        alert('Usuário ou senha incorretos!');
        return false;
    }
}

function register() {
    var username = document.getElementById('register-username').value;
    var email = document.getElementById('register-email').value;
    var password = document.getElementById('register-password').value;

    localStorage.setItem('username', username);
    localStorage.setItem('email', email);
    localStorage.setItem('password', password);

    alert('Cadastro bem-sucedido!');
    return true;
}
// Importando Vue 3
import { createApp } from 'vue';

// Definindo o componente Vue
const MyComponent = {
    template: '<div>Este é o meu componente Vue!</div>'
};

// Criando a aplicação Vue
const app = createApp({});

// Registrando o componente Vue
app.component('my-component', MyComponent);

// Montando a aplicação Vue
app.mount('#app');