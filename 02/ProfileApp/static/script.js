const panelArray = Array.from(document.querySelectorAll(".panel"));
console.log(panelArray);
panelArray.forEach(element => {
    element.addEventListener("click", toggleOpen)
});

function toggleOpen() {
    this.classList.toggle('open');
}