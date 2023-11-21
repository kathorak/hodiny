let input = parseInt(prompt("Zadej věk"))

if(input < 0){
    console.log("Lžete")}
else if(input > 100){
    console.log("Lžete") }
else if(input >= 21){
    console.log("Můžete si objednat cokoliv")}
else if(input >= 18){
        console.log("Můžete si objednat cokoliv, pokud nejste Američan")}
else{
    console.log("Můžete si objednat jen nealko")}