let tlacitko = document.querySelector("#tlacitko") //hledá v celém html, universální
let meniciText = document.getElementById("meniciText") //vždy hledá jen id
let input = document.querySelector("#text")
let body = document.querySelector("#body")

console.log(input)
tlacitko.addEventListener("click", zmenText)
function zmenText(){
    let textInputu = input.value
    //console.log(textInputu)
    if(textInputu==="pes"){
        meniciText.innerText = "Psi jsou best"
        body.style.background = "red"
    }
    else if(textInputu==="kočka"){
        meniciText.innerText = "Čočky jsou cool"
        body.style.background = "orange"
    }
    else if(textInputu==="papoušek"){
        meniciText.innerText = "🦜"
        body.style.background = "yellow"
    }
    else if(textInputu==="ovce"){
        meniciText.innerText = "🐑"
        body.style.background = "green"
    }
    else{
        meniciText.innerText = "Toto zvíře neznám:("
        body.style.background = "grey"
    }
}
