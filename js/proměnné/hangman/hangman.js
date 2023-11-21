const nadpis = document.querySelector("#nadpis"),
    text = document.querySelector("#text"),
    tlacitko = document.querySelector("#tlacitko"),
    input = document.querySelector("#input"),
    pokusy = document.querySelector("#pocetPokusu")

const seznamSlov = ["hokus", "pokus", "pes", "les"]
let hadaneSlovo = seznamSlov[Math.floor(Math.random() * seznamSlov.length)]
console.log(hadaneSlovo)

let odpoved = []

for (let i = 0; i < hadaneSlovo.length; i++) {
    odpoved[i] = "_"
}

for (let i = 0; i < odpoved.length; i++) {
    text.innerText += odpoved[i]
}

let pocetPokusu = 0
let uhodnuto = false

tlacitko.addEventListener("click", hadani)

function hadani() {
    uhodnuto = false
    let pismeno = input.value
    input.value = ""
    for (let i = 0; i < hadaneSlovo.length; i++) {
        if (pismeno === hadaneSlovo[i]) {
            odpoved[i] = pismeno
            uhodnuto = true
        }
    }
    text.innerText = ""
    for (let i = 0; i < odpoved.length; i++) {
        text.innerText += odpoved[i]
    }

    if (uhodnuto === false) {
        pocetPokusu++
        pokusy.innerText = pocetPokusu

        if (pocetPokusu === 1) {
            s1.style.display = "block"
        }
        if (pocetPokusu === 2) {
            s1.style.display = "none"
            s2.style.display = "block"
        }
        if (pocetPokusu === 3) {
            s2.style.display = "none"
            s3.style.display = "block"
        }
        if (pocetPokusu === 4) {
            s3.style.display = "none"
            s4.style.display = "block"
        }
        if (pocetPokusu === 5) {
            s4.style.display = "none"
            s5.style.display = "block"
        }
        if (pocetPokusu === 6) {
            s5.style.display = "none"
            s6.style.display = "block"
        }
        if (pocetPokusu === 7) {
            s6.style.display = "none"
            s7.style.display = "block"
        }
        if (pocetPokusu === 8) {
            s7.style.display = "none"
            s8.style.display = "block"
        }
    }
}
