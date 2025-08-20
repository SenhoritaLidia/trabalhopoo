// 01 
const saudar = (nome) => `Olá, ${nome}!`;
console.log(saudar("Lidia"));

// 02 
function executarOperacao(num1, num2, callback) {
  return callback(num1, num2);
}

const somar = (a, b) => a + b;
const multiplicar = (a, b) => a * b;

console.log("Soma:", executarOperacao(5, 3, somar));
console.log("Multiplicação:", executarOperacao(5, 3, multiplicar));

// 03 
function exibirMensagem(nome, callback) {
  return callback(nome);
}

const mensagemDeBoasVindas = (nome) => `Seja bem-vindo, ${nome}!`;
const mensagemDeDespedida = (nome) => `Até logo, ${nome}!`;

console.log(exibirMensagem("Lidy", mensagemDeBoasVindas));
console.log(exibirMensagem("Lidy", mensagemDeDespedida));

// 04 
function verificarNumero(numero) {
  return new Promise((resolve, reject) => {
    if (numero >= 0) {
      resolve(`Número válido: ${numero}`);
    } else {
      reject("Erro: número negativo não é permitido");
    }
  });
}

verificarNumero(10)
  .then((res) => console.log(res))
  .catch((err) => console.log(err));

verificarNumero(-5)
  .then((res) => console.log(res))
  .catch((err) => console.log(err));

// 05 
function consultarPaciente(nome) {
  return new Promise((resolve, reject) => {
    if (nome.trim() !== "") {
      resolve(`Consulta para ${nome} agendada com sucesso.`);
    } else {
      reject("Erro: nome do paciente não pode ser vazio.");
    }
  });
}

consultarPaciente("Maria")
  .then((res) => console.log(res))
  .catch((err) => console.log(err));

consultarPaciente("")
  .then((res) => console.log(res))
  .catch((err) => console.log(err));

// 06 
async function agendarConsulta(nome) {
  try {
    const resultado = await consultarPaciente(nome);
    console.log(resultado);
  } catch (erro) {
    console.log(erro);
  }
}

agendarConsulta("João");
agendarConsulta("");

// 07 
function verificarHorario(hora) {
  return new Promise((resolve, reject) => {
    if (hora >= 8 && hora <= 18) {
      resolve("Estamos em horário de atendimento.");
    } else {
      reject("Fora do horário de atendimento.");
    }
  });
}

async function checarAtendimento(hora) {
  try {
    const resultado = await verificarHorario(hora);
    console.log(resultado);
  } catch (erro) {
    console.log(erro);
  }
}

checarAtendimento(10); // dentro do horário
checarAtendimento(22); // fora do horário
