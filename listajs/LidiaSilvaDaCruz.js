// 01 
console.log("Hello World!");

// 02 
let nome = "Lidia";
console.log("Olá, " + nome);

const nomeConst = "Lidia";
console.log(`Olá, ${nomeConst}`);

// 03
let a = 20;
let b = 6;

console.log("Soma:", a + b);
console.log("Subtração:", a - b);
console.log("Multiplicação:", a * b);
console.log("Divisão:", a / b);
console.log("Resto:", a % b);

console.log("Potência:", Math.pow(a, b));
console.log("Raiz quadrada de a:", Math.sqrt(a));
console.log("Arredondar b:", Math.ceil(b));

// 04 
let numero = 15;
if (numero % 2 === 0) {
  console.log(numero + " é par");
} else {
  console.log(numero + " é ímpar");
}

// 05 
let hora = 23;
if (hora >= 6 && hora < 12) {
  console.log("Bom dia!");
} else if (hora >= 12 && hora < 18) {
  console.log("Boa tarde!");
} else if (hora >= 18 && hora < 24) {
  console.log("Boa noite!");
} else {
  console.log("Boa madrugada!");
}

// 06 
let numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let pares = [];
let impares = [];

for (let n of numeros) {
  if (n % 2 === 0) {
    pares.push(n);
  } else {
    impares.push(n);
  }
}
console.log("Pares:", pares);
console.log("Ímpares:", impares);

// 07 
function quadrado(num) {
  return num * num;
}
console.log("Quadrado de 5:", quadrado(5));

// 08 
function maioresQueDez(array) {
  return array.filter(num => num > 10);
}
console.log(maioresQueDez([5, 12, 8, 20, 15, 3]));

// 09 
let idade = 18;
if (idade >= 0 && idade <= 12) {
  console.log("Criança");
} else if (idade >= 13 && idade <= 17) {
  console.log("Adolescente");
} else if (idade >= 18 && idade <= 59) {
  console.log("Adulto");
} else if (idade >= 60) {
  console.log("Idoso");
} else {
  console.log("Idade inválida");
}

// 10 
function executarDepois(callback) {
  console.log("Aguardando 3 segundos...");
  setTimeout(() => {
    console.log("Executando callback...");
    callback();
    console.log("Callback finalizado!");
  }, 3000);
}

executarDepois(() => {
  console.log("Sou o callback! ✅");
});
