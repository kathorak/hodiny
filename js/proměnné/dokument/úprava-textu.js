let tlacitko = document.querySelector("#tlacitko") //hledá v celém html, universální
let nadpis = document.getElementById("nadpis") //vždy hledá jen id
let input = document.querySelector("#input")


tlacitko.addEventListener("click", zmenText) //naslouchač - "jaké události naslouchá", funkce
function zmenText() { //vytvoříme funkci
    let textInputu = input.value
    nadpis.style.color = "red" 
    nadpis.style.fontSize = "100pt" //zvětšení textu
    nadpis.innerText = textInputu //změna textu
} 