// 1000 - Hello World!
console.log("Hello World!")

// // 1001 - Extremamente Básico
// const readline1001 = require('readline').createInterface({
//     input: process.stdin,
//     output: process.stdout
// })
// readline1001.question(``, num1 => {
//     readline1001.question(``, num2 => {
//         let res = Number(num1) + Number(num2);
//         console.log(`X = ${res}`)
//     })
// })


// 1002 - Área do Círculo 
// const readline1002 = require('readline').createInterface({
//     input: process.stdin,
//     output: process.stdout
// })
// readline1002.question(raio =>{
//         let area = 3.141
// })

// 1003 - Soma Simples
const readline1003 = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
})
readline1003.question(``, a => {
    readline1003.question(``, b =>{
        let soma = parseInt(a) + parseInt(b);
        console.log("SOMA = " + soma);
    })
})

// 1004 - Produto simples
