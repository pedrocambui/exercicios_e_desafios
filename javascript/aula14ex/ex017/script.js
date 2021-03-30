function gerar(){
    var num = document.getElementById('ntxt')
    var res = document.getElementById('res')
    let tab = document.getElementById('seltab')
    if(num.value.length ==0){
        window.alert('Por favor, digite um número!')
    }else{
        n = Number(num.value)
        tab.innerHTML =' '
        for(var c =0; c <= 10; c++){
            let item = document.createElement('option')
            item.text = `${n} x ${c} = ${n * c}`
            item.value = `tab${c}`
            tab.appendChild(item)
        }
    }
}


/*
function gerar(){
    var ntxt = document.getElementById('ntxt')
    var res = document.getElementById('res')
    n = Number(ntxt.value)
    if(ntxt.value.length ==0){
        window.alert('ERRO')
    }else{
        res.innerHTML = ''
        for(var c =0; c <= 10; c++){
            res.innerHTML += `${n} x ${c} = ${n * c} <br>`
        }
    }
}
*/