// Получаем блок с классом "answer"
var answerBlock = document.querySelector('form');

// Получаем список всех <label> элементов внутри блока "answer"
var labels = answerBlock.querySelectorAll('label');

// Преобразуем NodeList в массив, чтобы использовать методы массивов
var labelsArray = Array.from(labels);

// Перемешиваем порядок элементов в массиве
labelsArray.sort(function() {
  return 0.5 - Math.random();
});

// Удаляем все <label> элементы из блока "answer"
labels.forEach(function(label) {
  label.remove();
});

// Добавляем перемешанные <label> элементы обратно в блок "answer"
labelsArray.forEach(function(label) {
  answerBlock.appendChild(label);
});
