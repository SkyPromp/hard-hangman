// display the image and the pattern
function display(mistakes, pattern) {
    // display the pattern
    if (!(document.getElementById("pattern"))) {
        let pattern_view = document.createElement("h1");
        pattern_view.id = "pattern";
        pattern_view.align = "center";
        document.body.appendChild(pattern_view);
    }
    document.getElementById("pattern").innerHTML = pattern.replaceAll(".", "_").split('').join(' ');


    // display the image
    if (!(document.getElementById("image"))) {
        let image = document.createElement("IMG");
        image.id = "image";
        image.width = "268";
        image.height = "415";
        image.align = "center";
        image.className = "imageplacement"
        document.body.appendChild(image);
    }
    document.getElementById("image").src = `afbeeldingen/galgje${mistakes}.png`;
}

// set the variables to empty values
let mistakes = 0;
let guesses = "";
let pattern = "";

// set the starting position of the game
fetch(`cgi-bin/game.cgi?guesses=&pattern=&mistakes=0&letter=Q`)
            .then(antwoord => antwoord.json()) // convert response to json
            .then(data => {
                pattern = data["pattern"].replaceAll("Q", ".");
                display(0, data["pattern"].replaceAll("Q", "."));
            });


// generate table
let table = document.createElement("TABLE");

// generate all the buttons
for (let letter = 65; letter < 91; letter++) {
    let btn = document.createElement("button");

    btn.innerHTML = String.fromCharCode(letter);
    btn.onclick = function () {
        // get the game data
        fetch(`cgi-bin/game.cgi?guesses=${guesses}&pattern=${pattern}&mistakes=${mistakes.toString()}&letter=${btn.textContent}`)
            .then(antwoord => antwoord.json()) // convert response to json
            .then(data => {
                mistakes = data["mistakes"];
                guesses = data["guesses"];
                pattern = data["pattern"];
                // check if the player has won
                if (!(pattern.includes("."))){
                    document.getElementById("body").innerHTML = "<br><h1 align='center'>Congratulations, you won!</h1><h2 align='center' onclick='window.location.reload();'>Click here to retry!</h2>>";
                }
                // check if the player has lost
                if(mistakes <= 9){
                    display(mistakes, pattern);
                } else{
                    document.getElementById("body").innerHTML = "<br><h1 align='center'>Too bad, you lost!</h1><h2 align='center' onclick='window.location.reload();'>Click here to retry!</h2>>";
                }

            });
        //disable the button
        btn.disabled = true; // disable the button
    };
    table.appendChild(btn)
    let space = document.createElement("span");
    space.innerHTML = " ";
    table.appendChild(space);

    // check if the table needs to go onto the next row
    if (letter === 75 || letter === 86) {
        table.align = "center";
        document.body.appendChild(table);
        table = document.createElement("TABLE");
        document.body.appendChild(document.createElement("br"));
    }

}
table.align = "center";
document.body.appendChild(table);