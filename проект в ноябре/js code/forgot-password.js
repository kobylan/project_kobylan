const loginForm = document.getElementById('login_form');
const loginButton = document.getElementById('login_button');

loginButton.addEventListener('click', () => {
  loginForm.classList.add('animated');
  setTimeout(() => {
    loginForm.classList.remove('animated');
  }, 500);
});
