// Funciones básicas de operaciones
function sumar(a, b) {
    return a + b;
}

function restar(a, b) {
    return a - b;
}

function multi(a, b) {
    return a * b;
}

function divi(a, b) {
    if (b === 0) {
        return "Error: División por cero";
    }
    return a / b;
}

// Función de saludo
function saludo() {
    console.log("¡Hola! Bienvenido a la Calculadora Interactiva.");
    document.getElementById('mensaje').textContent = "¡Hola! Bienvenido a mi calculadora.";
}

// Función verificar si un número es par
function par(numero) {
    return numero % 2 === 0;
}

// Función calculadora principal
function calculadora(n1, n2, operacion) {
    switch (operacion) {
        case 'sumar':
            return sumar(n1, n2);
        case 'restar':
            return restar(n1, n2);
        case 'multi':
            return multi(n1, n2);
        case 'divi':
            return divi(n1, n2);
        default:
            return "Operación no válida...";
    }
}

// Función principal de cálculo
function calcular() {
    // Llamar a la función de saludo
    saludo();

    // Obtener valores
    let numero1 = parseFloat(document.getElementById('numero1').value);
    let numero2 = parseFloat(document.getElementById('numero2').value);
    let operacion = document.getElementById('operacion').value;

    // Verificar si los números son válidos
    if (isNaN(numero1) || isNaN(numero2)) {
        document.getElementById('resultado').textContent = "Por favor, ingrese números válidos";
        return;
    }

    // Realizar cálculo
    let resultado = calculadora(numero1, numero2, operacion);

    // Mostrar resultado
    document.getElementById('resultado').textContent = `Resultado: ${resultado}`;
    
    // Verificar si el primer número es par
    let esPar = par(numero1);
    console.log(`¿Es ${numero1} un número par? ${esPar}`);
}

// Ejecutar saludo al cargar la página
window.onload = saludo;
