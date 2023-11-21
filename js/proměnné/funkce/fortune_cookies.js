let tlacitko = document.querySelector("#tlacitko")
let predpoved = document.querySelector("#predpoved")

tlacitko.addEventListener("click", zmenText)
function zmenText() {
    let a
    a = 1 + Math.round(Math.random() * 5)
    if (a === 1) {
        predpoved.innerText = "Budeš mít štěstí"
    }
    if (a === 2) {
        predpoved.innerText = "Najdeš lásku"
    }
    if (a === 3) {
        predpoved.innerText = "Obdržíš hodně peněz"
    }
    if (a === 4) {
        predpoved.innerText = "Onemocníš"
    }
    if (a === 5) {
        predpoved.innerText = "Koupíš si psa"
    }
}
