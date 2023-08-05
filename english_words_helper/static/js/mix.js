var answerBlock = document.querySelector('form');

var labels = answerBlock.querySelectorAll('label');

var labelsArray = Array.from(labels);

labelsArray.sort(function() {
  return 0.5 - Math.random();
});

labels.forEach(function(label) {
  label.remove();
});

labelsArray.forEach(function(label) {
  answerBlock.appendChild(label);
});
