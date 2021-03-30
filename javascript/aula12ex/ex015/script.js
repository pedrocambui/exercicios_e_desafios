function verificar(){
    var data = new Date()
    var atual = data.getFullYear()
    var nascimento = Number(window.document.getElementById('txtano').value)
    var res = document.getElementById('res')
    var img = document.createElement('img')
    img.setAttribute('id', 'foto')
    if (nascimento == 0 || nascimento > atual){
        alert('ERRO. Verifique os dados e tente novamente!')
    }else{
        var idade = atual - nascimento
        var fsex = window.document.getElementsByName('radsex')
        var genero = ''
        if (fsex[0].checked){
            genero = 'Homem'
            if(idade >= 0 && idade <= 12){
                img.src = 'bebe-homem.png'
            }else if (idade < 21){
                img.src = 'jovem-homem.png'
            }else if (idade < 50){
                img.src = 'adulto-homem.png'
            }else {
                img.src ='velho-homem.png'
            }
        } else if (fsex[1].checked){
            genero = 'Mulher'
            if (idade <= 12){
                img.src = 'bebe-mulher.png'
            }else if (idade <21){
                img.src = 'jovem-mulher.png'
            }else if (idade < 50){
                img.src = 'adulto-mulher.png'
            }else{
                img.src = 'velho-mulher.png'
            }
        }else{
            window.alert('ERRO. Porfavor selecione o sexo!')
        }
    }
    res.style.textAlign = 'center'
    res.innerHTML = `Detectamos ${genero} com ${idade} anos.`
    res.appendChild(img)
    
}