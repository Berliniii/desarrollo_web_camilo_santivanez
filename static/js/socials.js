function revisaCheck(element){
    if(element.checked){
        document.getElementById(element.name).style.display = "block";
    }
    else{
        document.getElementById(element.name).style.display = "none";
    }
}

function subirFoto(element) {
    // Obtener el número actual de la foto (último carácter del id)
    const currentNum = parseInt(element.id.slice(-1));
    
    // Dar la opcion de ingresar otra foto
    const nextInput = document.getElementById(`foto${currentNum + 1}`);
    if (nextInput) {
        nextInput.style.display = "block";
    }
}