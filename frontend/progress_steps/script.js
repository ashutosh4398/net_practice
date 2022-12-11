const progress = document.querySelector("#progress")
const prev = document.querySelector("#prev")
const next = document.querySelector("#next")
const circles = document.querySelectorAll(".circle")

let currentActiveCircle = 1

next.addEventListener('click', () => {
    currentActiveCircle ++
    if (currentActiveCircle > circles.length) {
        currentActiveCircle = circles.length
    }
    update();
})

prev.addEventListener('click', () => {
    currentActiveCircle --;
    if (currentActiveCircle < 1) {
        currentActiveCircle = 1;
    }
    update();
})

const update = () => {
    circles.forEach((circle, index) => {
        if (index < currentActiveCircle) {
            circle.classList.add('active')
        } else {
            circle.classList.remove('active')
        }
    })
    const actives = document.querySelectorAll(".circle.active")
    progress.style.width = ((actives.length-1)/(circles.length-1)*100) + "%";
    
    if (currentActiveCircle == 1) {
        prev.disabled = true;
    } else if (currentActiveCircle == circles.length) {
        next.disabled = true;
    } else {
        prev.disabled = false;
        next.disabled = false;
    }
}