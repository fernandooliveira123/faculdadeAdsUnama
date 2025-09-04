// const titulo = document.querySelector('#titulo');
// titulo.innerHTML = 'Minha página';
// titulo.style.color = 'green';
// titulo.classList.add('bg-info');
// titulo.classList.add('p-3');

const botao = document.querySelector('#meu-botao');

// Eventos Js
botao.addEventListener('mouseover', function acao() {
  const titulo = document.querySelector('#titulo');
  titulo.innerHTML = 'Minha página';
  titulo.style.color = 'green';
  titulo.classList.add('bg-info');
  titulo.classList.add('p-3');

  // alert('teste')
});

function criar() {
  const lista = document.querySelector('ol');
  const item = document.createElement('li');
  item.innerHTML = 'Trabalho';
  lista.appendChild(item); 
}
