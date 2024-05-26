// 1000 - Hello World!
console.log("Hello World!")

// 1001 - Extremamente Básico
function j1001(n1,n2){
    console.log(`X = ${n1+n2}`)
}

// 1002 - Área do Círculo 
function j1002(raio){
    let area = 3.14159 * (raio**2)
    console.log(`A=${area.toFixed(4)}`)
}

// 1003 - Soma Simples
function j1003(a,b) {
    console.log(`SOMA = ${a+b}`)
}

// 1004 - Produto simples
function j1004(x,y){
    console.log(`PROD = ${x*y}`)
}

// 1005 - Média 1
function j1005(n1,n2){
    let media = ((n1 * 3.5) + (n2 * 7.5))/11
    console.log(`MEDIA = ${media.toFixed(5)}`)
}

// 1006 - Média 2
function j1006(n1,n2,n3){
    let media = (n1 * 0.2) + (n2 * 0.3) + (n3 * 0.5)
    console.log(`MEDIA = ${media.toFixed(1)}`)
}

// 1007 - Diferença
function j1007(a,b,c,d){
    console.log(`DIFERENCA = ${(a*b)-(c*d)}`)
}

// 1008 - Salário
function j1008(n, h, s){
    console.log(`NUMBER = ${n}`)
    console.log(`SALARY = U$ ${(h*s).toFixed(2)}`)
}

// 1009 - Salário com bônus
function j1009(nome, sal, ven){
    let total = sal + (ven * 0.15)
    console.log(`TOTAL = R$ ${total.toFixed(2)}`)
}

// 1010 - Cálculo simples
function j1010(p1,p2){
    
}

// 1153 - Fatorial Simples
function j1153(n){
    let x = 1
    while (n > 0){
        x*=n
        n--
    }
    console.log(x)
}


