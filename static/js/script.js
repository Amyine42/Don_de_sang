const path_men = document.querySelector(".menvector path");
const path_female = document.querySelector(".femalevector path");

path_men.addEventListener('click', () => {
  path_men.setAttribute('fill', 'skyblue');
  path_female.setAttribute('fill', 'black');
});

path_female.addEventListener('click', () => {
  path_female.setAttribute('fill', 'pink');
  path_men.setAttribute('fill', 'black');
});

let btn_clicked = document.querySelectorAll(".blood_type_selection div") 

btn_clicked.forEach(function(element) {
    element.onclick = function () {
        btn_clicked.forEach(function(element) {
            element.style.backgroundColor = ""
        })
       this.style.backgroundColor = "#EF3054";
    };
})

const container_hide = document.querySelector(".submit")
const container = document.querySelector(".container")
const thanksmsg = document.querySelector(".thanks_message")
const paragrapghmsg = document.querySelector(".thanks_paragraph")
const submit_paragrapgh = document.querySelector(".thanks_message_submit")


container_hide.addEventListener('click', () => {
    container.style.display = 'none' 
    thanksmsg.style.display = 'none'
    paragrapghmsg.style.display = 'none'
    submit_paragrapgh.style.display = 'block'
})