let tlacitko = document.querySelector("#tlacitko")
let meniciText = document.querySelector("#meniciText")
let jmeno = document.querySelector ("#jmeno")
let zvire = document.querySelector ("#zvire")
let jidlo = document.querySelector ("#jidlo")

tlacitko.addEventListener("click", zmenText)

function zmenText(){
    meniciText.innerText = jmeno.value + " má rád/a " + zvire.value + " jako " + jidlo.value
}