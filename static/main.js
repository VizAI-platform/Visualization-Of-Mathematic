let bod = document.body
let elm = document.querySelector(".mouscursor")




bod.addEventListener("mousemove" , e => {
    console.log(bod)
    elm.style.left = e.clientX - 40
    elm.style.top = e.clientY - 40
    console.log(e.clientX + 300 , e.clientY + 300)
    
})
let hoveredbox = document.querySelector(".trigonometry")
hoveredbox.addEventListener(
    "mousemove" , e => {
        console.log(e)
        elm.classList.add("bluehov")
        
    }
)
hoveredbox.addEventListener("mouseout" , e => {
    elm.classList.remove("bluehov")
})



