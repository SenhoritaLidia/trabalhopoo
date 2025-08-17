// Questão 1
function Questao_1() {
    const mensagem = "Bem-vindo à nossa loja online!";
    console.log(mensagem);
}

// Questão 2
function Questao_2() {
    let nomeProduto = "Tênis Esportivo";       
    const precoProduto = 199.99;               
    let disponivel = true;                      
    console.log("Produto:", nomeProduto);
    console.log("Preço:", precoProduto);
    console.log("Disponível?", disponivel);
}

// Questão 3
function Questao_3() {
    let preco = 200;
    let desconto = 0.1; 
    let quantidade = 3;

    let precoComDesconto = preco - (preco * desconto); 
    let precoTotal = precoComDesconto * quantidade; 
    let precoComAcrescimo = precoTotal + 20;          

    console.log("Preço com desconto:", precoComDesconto);
    console.log("Preço total:", precoTotal);
    console.log("Preço total com taxa:", precoComAcrescimo);
}

// Questão 4
function Questao_4() {
    let cliente = "Lidia";
    const mensagem = `Bem-vinda à nossa loja online, ${cliente}!`;
    console.log(mensagem);
}

// Questão 5
function Questao_5() {
    let carrinho = ["Camisa", "Calça", "Tênis", "Boné"];
    let indiceExcluir = 2; 
    let itemRemovido = carrinho.splice(indiceExcluir, 1);
    console.log(`O item removido do carrinho foi: ${itemRemovido}`);
    console.log("Carrinho atualizado:", carrinho);
}

// Questão 6
function Questao_6() {
    let precoProduto = 150;
    let dinheiroCliente = 200;

    if (dinheiroCliente >= precoProduto) {
        console.log("Compra realizada com sucesso!");
    } else {
        console.log("Saldo insuficiente para a compra.");
    }
}

// Questão 7
function Questao_7() {
    let estoque = 0;
    const limiteEstoque = 5;

    while (estoque < limiteEstoque) {
        estoque++;
        console.log(`Produto adicionado ao estoque. Total agora: ${estoque}`);
    }
}

// Questão 8
function Questao_8() {
    function boasVindas(cliente) {
        return `Bem-vindo à nossa loja online, ${cliente}!`;
    }

    function calcularDesconto(preco, desconto) {
        return preco - (preco * desconto);
    }

    console.log(boasVindas("Lidy"));
    console.log("Preço com desconto de 10%:", calcularDesconto(200, 0.1));
}

// Questão 9
function Questao_9() {
    let produto = {
        nome: "Camiseta Polo",
        preco: 79.9
    };

    let cliente = {
        nome: "Lidy",
        email: "lidy@email.com"
    };

    console.log("Produto:", produto);
    console.log("Cliente:", cliente);
}

// Questão 10
function Questao_10() {
    function pagamentoParcelado(preco, parcelas) {
        let valorParcela = preco / parcelas;
        return `Preço total: R$${preco.toFixed(2)}, em ${parcelas} parcelas de R$${valorParcela.toFixed(2)} cada.`;
    }

    function pagamentoComDesconto(preco, desconto) {
        let precoFinal = preco - (preco * desconto);
        return `Preço original: R$${preco.toFixed(2)}, com desconto de ${desconto * 100}%: R$${precoFinal.toFixed(2)}`;
    }

    console.log(pagamentoParcelado(300, 3));
    console.log(pagamentoComDesconto(300, 0.15));
}

// Chamando todas as funções para testar
Questao_1();
Questao_2();
Questao_3();
Questao_4();
Questao_5();
Questao_6();
Questao_7();
Questao_8();
Questao_9();
Questao_10();
