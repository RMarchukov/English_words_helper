document.addEventListener("DOMContentLoaded", function() {
  var levelBlocks = document.querySelectorAll(".level-block");

  levelBlocks.forEach(function(block) {
    var levelHeading = block.querySelector(".level-heading");
    var topics = block.querySelector(".topics");

    levelHeading.addEventListener("click", function() {
      topics.style.display = topics.style.display === "none" ? "block" : "none";
    });
  });
});
