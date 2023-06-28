document.addEventListener('DOMContentLoaded', function() {
  var words = document.querySelectorAll('.word');
  words.forEach(function(word) {
    word.addEventListener('click', function() {
      this.classList.toggle('active');
    });
  });
});
