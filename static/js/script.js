const label_men = document.querySelector(".menvector");
const label_female = document.querySelector(".femalevector");

label_men.addEventListener('click', () => {
  label_men.querySelector("path").setAttribute("fill", "skyblue");
  label_female.querySelector("path").setAttribute("fill", "black");
});

label_female.addEventListener('click', () => {
  label_female.querySelector("path").setAttribute("fill", "pink");
  label_men.querySelector("path").setAttribute("fill", "black");
});

let btn_clicked = document.querySelectorAll(".blood_type_selection div")

btn_clicked.forEach(function(element) {
    element.onclick = function () {
        element.querySelector("label").click();
        btn_clicked.forEach(function(element) {
            element.style.backgroundColor = ""
        })
       element.style.backgroundColor = "#EF3054";
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
