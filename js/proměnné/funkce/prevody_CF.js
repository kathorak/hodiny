let tlacitko = document.querySelector("#tlacitko")
let stupne = document.querySelector("#stupne")
let hodnota = parseInt(document.querySelector("#hodnota"))
let prevod = document.querySelector("#prevod")

tlacitko.addEventListener("click", tretiFCE)

function prevadeniC(C) {
    let F = (9 / 5) * C + 32
    return F
}

function prevadeniF(F) {
    let C = (F - 32) / 1.8
    return C
}

function tretiFCE() {
    let vysledek
    if (stupne === "C") {
        vysledek = prevadeniC(hodnota)
    } else if (stupne === "F") {
        vysledek = prevadeniF(hodnota)
    }

    return "Něco se nepovedlo"
}

console.log(tretiFCE(hodnota, stupne))
