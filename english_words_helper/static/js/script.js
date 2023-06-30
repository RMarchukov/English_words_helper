document.addEventListener('DOMContentLoaded', function() {
    words = document.querySelectorAll('.word');
    words.forEach(function(word) {
        word.addEventListener('click', function() {
            this.classList.toggle('transform');
        });
    });
});
