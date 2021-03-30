function gerar(){
    var num = window.document.getElementById('ntxt')
    var res = window.document.getElementById('res')
    var tab = window.document.getElementById('seltab')
    if(num.value.length == 0){
        window.alert('Por favor, digite um número.')
    }else{
        n = Number(num.value)
        tab.innerHTML = ''
        var c= 1
        while (c <= 10){
            var item = window.document.createElement('option')
            item.text = `${n} x ${c} = ${n * c}`
            item.value = `val${c}`
            tab.appendChild(item)
            c ++
        }

    }
}