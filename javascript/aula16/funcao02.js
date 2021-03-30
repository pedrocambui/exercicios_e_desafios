valores =[5, 7, 9]
num = 5
if(valores.indexOf(num) != -1){
    console.log('nao vou adicionar')
}else{
    valores.push(num)
}
console.log(valores)

/*
function soma(n1=0, n2=0){
    return n1 + n2
}
console.log(soma(7, 3))
*/