var valores = []
var res = window.document.getElementById('res')
function adicionar(){
    var num = window.document.getElementById('num')
    if (num.value.length == 0 || num.value <= 0 || num.value > 100 || valores.indexOf(num.value) != -1){
        window.alert('Valor inválido ou já encontrado na lista.')
    }else{
        var n = num.value
        var tab = window.document.getElementById('seltab')
        var item = window.document.createElement('option')
        item.text = `Valor ${n} adicionado.`
        tab.appendChild(item)
        valores.push(n)
        res.innerHTML = ''
    }
    num.value = ''
    num.focus()
}

function finalizar(){
    if (valores.length == 0){
        window.alert('Adicione valores antes de finalizar!')
    }else{
        res.innerHTML = `<p>Ao todo temos ${valores.length} números cadastrados.</p>`
        let maior = valores[0]
        let menor = valores[0]
        let soma = 0
        for (let pos in valores){
            if (valores[pos] > maior){
                maior = valores[pos]
            }
            if (valores[pos < menor])
            menor = valores[pos]
            soma += Number(valores[pos])
        }
        res.innerHTML += `<p>O menor valor informado é ${menor}</p>`
        res.innerHTML += `<p>O maior valor informado é ${maior}</p>`
        res.innerHTML += `<p>Somando todos os valores, temos ${soma}</p>`
        res.innerHTML += `<p>A média dos valores digitados é ${soma / valores.length}</p>`
    }
}
