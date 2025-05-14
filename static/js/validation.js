const validateName = (name) => {
    if(!name) return false;
    let lengthValid = name.trim().length <= 200;
    
    return lengthValid;
  }
  
  const validateEmail = (email) => {
    if (!email) return false;
    let lengthValid = email.length < 100;
  
    // validamos el formato
    let regex = /^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    let formatValid = regex.test(email);
  
    // devolvemos la lógica AND de las validaciones.
    return lengthValid && formatValid;
  };
  
  const validatePhoneNumber = (phoneNumber) => {
    const isEmpty = !phoneNumber || phoneNumber.trim() === "";
    const isValidFormat = /^\+569\.\d{8}$/.test(phoneNumber);
    
    return isEmpty || isValidFormat;
  };

  // Prellenar fechas al cargar la página
  document.addEventListener('DOMContentLoaded', function() {
    const fechaInicioInput = document.getElementById('dia-hora-inicio');
    const fechaTerminoInput = document.getElementById('dia-hora-termino');
    
    // Obtener fecha actual y formatear para el input
    const ahora = new Date();
    const fechaActual = new Date(ahora.getTime() - ahora.getTimezoneOffset() * 60000).toISOString().slice(0, 16);
    
    // Prellenar fecha de inicio con la actual
    fechaInicioInput.value = fechaActual;
    
    // Prellenar fecha de término con 3 horas después
    const fechaMas3Horas = new Date(ahora.getTime() + 3 * 60 * 60 * 1000);
    const fechaTermino = new Date(fechaMas3Horas.getTime() - fechaMas3Horas.getTimezoneOffset() * 60000).toISOString().slice(0, 16);
    fechaTerminoInput.value = fechaTermino;
    
    // Validar al enviar el formulario
    document.getElementById('informar_actividad').addEventListener('submit', function(e) {
        if (!validarFechas()) {
            e.preventDefault(); // Detener el envío si la validación falla
        }
    });
});

// Validación de fecha y hora de inicio y término
function validarFechas() {
    const fechaInicioInput = document.getElementById('dia-hora-inicio');
    const fechaTerminoInput = document.getElementById('dia-hora-termino');
    
    // Validar que la fecha de inicio tenga valor
    if (!fechaInicioInput.value) {
        return false;
    }
    
    // Prellenar fecha de término con 3 horas después de la fecha de inicio
    const fechaInicio = new Date(fechaInicioInput.value);
    const fechaTerminoAuto = new Date(fechaInicio.getTime() + (3 * 60 * 60 * 1000)); // Sumar 3 horas en milisegundos
    
    // Validar que la fecha de término sea mayor que la de inicio
    if (fechaTerminoInput.value) {
        const fechaTermino = new Date(fechaTerminoInput.value);
        
        if (fechaTermino <= fechaInicio) {
            return false;
        }
    }
    
    return true; // Todas las validaciones pasaron
}
  
  const validateFiles = (files) => {
    if (!files) return false;
  
    // validación del número de archivos
    let lengthValid = 1 <= files.length && files.length <= 5;
  
    // validación del tipo de archivo
    let typeValid = true;
  
    for (const file of files) {
      // el tipo de archivo debe ser "image/<foo>" o "application/pdf"
      let fileFamily = file.type.split("/")[0];
      typeValid &&= fileFamily == "image" || file.type == "application/pdf";
    }
  
    // devolvemos la lógica AND de las validaciones.
    return lengthValid && typeValid;
  };
  
  const validateSelect = (select) => {
    if(!select) return false;
    return true
  }
  
  //logica de validación
  const validateForm = () => {
    const myForm = document.forms["informar_actividad"];
    const name = myForm["nombre_organizador"].value;
    const email = myForm["email-organizador"].value;
    const phoneNumber = myForm["celu-organizador"].value;
    const region = myForm["select-region"].value;
    const comuna = myForm["select-comuna"].value;
    const fechaInicio = myForm["dia-hora-inicio"].value;
    const fechaTermino = myForm["dia-hora-termino"].value;
  
    // Archivos (filtramos los inputs visibles y con valor)
    const fileInputs = ["foto1", "foto2", "foto3", "foto4", "foto5"].map(id => document.getElementById(id));
    const validFiles = fileInputs.filter(input => input && input.files.length > 0).map(input => input.files[0]);
  
    const invalidInputs = [];
    let isValid = true;
    const setInvalidInput = (inputName) => {
      invalidInputs.push(inputName);
      isValid = false;
    };
  
    if (!validateSelect(region)) setInvalidInput("Región");
    if (!validateSelect(comuna)) setInvalidInput("Comuna");
    if (!validateName(name)) setInvalidInput("Nombre");
    if (!validateEmail(email)) setInvalidInput("Email");
    if (!validatePhoneNumber(phoneNumber)) setInvalidInput("Número de celular");
    if (!validarFechas(fechaInicio, fechaTermino)) setInvalidInput("Fechas");
    if (!validateFiles(validFiles)) setInvalidInput("Fotos (1 a 5 imágenes)");
  
    const validationBox = document.getElementById("val-box");
    const validationMessageElem = document.getElementById("val-msg");
    const validationListElem = document.getElementById("val-list");
  
    if (!isValid) {
      validationListElem.textContent = "";
      invalidInputs.forEach(input => {
        const li = document.createElement("li");
        li.innerText = input;
        validationListElem.appendChild(li);
      });
      validationMessageElem.innerText = "Los siguientes campos son inválidos:";
      validationBox.style.backgroundColor = "#ffdddd";
      validationBox.style.borderLeftColor = "#f44336";
      validationBox.hidden = false;
    } else {
      myForm.style.display = "none";
      validationMessageElem.innerText = "¡Formulario válido! ¿Está seguro de que desea agregar esta actividad?";
      validationListElem.textContent = "";
      validationBox.style.backgroundColor = "#ddffdd";
      validationBox.style.borderLeftColor = "#4CAF50";
  
      const submitButton = document.createElement("button");
      submitButton.innerText = "Si, estoy seguro";
      submitButton.style.marginRight = "10px";
      submitButton.addEventListener("click", () => {
        // No alcanzo a poner un boton de regreso :c, pondre un alert noma
        //alert("Hemos recibido su información, muchas gracias y suerte en su actividad")
        myForm.submit();
        validationBox.hidden = true;  
        myForm.style.display = "block";
      });
  
      const backButton = document.createElement("button");
      backButton.innerText = "No, no estoy seguro, quiero volver al formulario";
      backButton.addEventListener("click", () => {
        myForm.style.display = "block";
        validationBox.hidden = true;
      });
  
      validationListElem.appendChild(submitButton);
      validationListElem.appendChild(backButton);
      validationBox.hidden = false;
    }
  };
  
  document.getElementById('dia-hora-inicio').addEventListener('change', validarFechas);
  document.getElementById("submit-btn").addEventListener("click", validateForm);
  