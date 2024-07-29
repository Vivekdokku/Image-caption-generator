// static/script.js
document.getElementById("sampleBtn").addEventListener("click", function () {
  animateButtons();
  showOptions("Sample Images");
});

document.getElementById("uploadBtn").addEventListener("click", function () {
  animateButtons();
  showOptions("Upload an Image");
});

document.getElementById("randomBtn").addEventListener("click", function () {
  animateButtons();
  showOptions("Random Image");
});

document
  .getElementById("randomImageBtn")
  .addEventListener("click", function () {
    // Add logic to handle random image functionality
  });

document.getElementById("generateBtn").addEventListener("click", function () {
  // Add logic to handle caption generation
});

function animateButtons() {
  document.getElementById("button-container").classList.add("minimizeButtons");
}

function showOptions(selectedOption) {
  document.getElementById("options-container").classList.remove("hidden");
  document.getElementById("options-container").classList.add("fadeIn");
  document.getElementById(
    "options-container"
  ).innerHTML = `<div class="triangle-up"></div><button class="optionBtn">${selectedOption}</button>`;
}
