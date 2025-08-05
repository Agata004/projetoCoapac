const loginForm = document.getElementById('loginForm');

loginForm.addEventListener('submit', function (event) {
    event.preventDefault();

    const credencial = document.getElementById('credencial').value.trim();
    const senha = document.getElementById('senha').value.trim();

    const users = JSON.parse(localStorage.getItem('users')) || [];

    const user = users.find(user => user.credencial === credencial && user.senha === senha);

    function showToast(mensagem) {
        let toast = document.getElementById("toast");
        toast.innerText = mensagem;
        toast.className = "show";
        setTimeout(() => { toast.className = toast.className.replace("show", ""); }, 3000);
    }

    if (user) {
        showToast(`Bem-vindo, ${user.nome}!`);
        setTimeout(() => {
            toast.className = toast.className.replace("show", "");
            window.location.href = "inicio.html"}, 1500);
    } else {
        showToast('Credencial ou senha incorretos.');
    }

    sessionStorage.setItem('userLogado', JSON.stringify(user));

});
