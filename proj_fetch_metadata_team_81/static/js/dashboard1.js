const iconClick = document.querySelectorAll('.icon')
const dropDown = document.querySelectorAll('.dami');
const answer = document.querySelectorAll('.answer')


iconClick.forEach((element) => {
  element.addEventListener("click", () => {
    iconClick.forEach((e) => {
      e.classList.remove("clicked");
    });
    element.classList.add("clicked");
  });
});

dropDown.forEach((element) => {
  element.addEventListener("click", (e) => {
  e.currentTarget.firstElementChild.classList.toggle("close")
  e.currentTarget.lastElementChild.classList.toggle("open")
  e.currentTarget.parentElement.lastElementChild.classList.toggle("open-answer")
  });
});


