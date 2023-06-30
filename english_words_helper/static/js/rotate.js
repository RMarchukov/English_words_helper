document.addEventListener("DOMContentLoaded", function() {
    var blocks = document.querySelectorAll(".main-styles");

    blocks.forEach(function(block) {
      var levels = block.querySelector(".levels");
      var topics = block.querySelector(".topics");

      block.addEventListener("click", function() {
          this.classList.toggle('transform');
        });
    });
});
