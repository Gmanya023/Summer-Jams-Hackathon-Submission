var imgs = document.getElementById('disc');


if (imgs.style.animationPlayState == "") {
    imgs.style.animationPlayState ="paused";
}


var player = document.getElementById("audio");
console.log(audio);
player.addEventListener("play", function () {
    console.log(imgs.style.animationPlayState);
    if (imgs.style.animationPlayState == "running") {
        imgs.style.animationPlayState = "paused";
    } else if (imgs.style.animationPlayState == "paused") {
        imgs.style.animationPlayState = "running";
    }

});

player.addEventListener("pause", function () {
    console.log(imgs.style.animationPlayState);
    if (imgs.style.animationPlayState == "running") {
        imgs.style.animationPlayState = "paused";
    } else {
        imgs.style.animationPlayState = "running";
    }
});