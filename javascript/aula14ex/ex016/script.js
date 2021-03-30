function Contar(){
    var ini = window.document.getElementById('inicio')
    var fim = document.getElementById('fim')
    var passo = document.getElementById('passo')
    var res = document.getElementById('res')
    if (ini.value.length == 0 || fim.value.length == 0 || passo.value.length == 0){
        window.alert('ERRO! Por favor preencha todos os campos.')
        res.innerHTML = 'Preparando a contagem...'
    }else{
        res.innerHTML = 'Contando: <br>'
        let c = Number(ini.value)
        let f = Number(fim.value)
        let p = Number(passo.value)
        if (p <= 0){
            window.alert('Passo inválido! Considerando PASSO = 1')
            p = 1
        }
        if (f > c){
            for(c; c <= f; c += p){
                res.innerHTML += `${c} \u{1F449} `
            }
        }else{
            for(c; c >= f; c -= p){
                res.innerHTML += `${c} \u{1F449} `
            }
        }
        res.innerHTML += '\u{1F3C1}'
    }

}
