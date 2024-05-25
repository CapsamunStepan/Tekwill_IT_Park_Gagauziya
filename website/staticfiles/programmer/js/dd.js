const header = document.querySelector('header');
const url = window.location.href;
const desiredColor = "#ffc600";
const keywordsToIndex = {
  'news': 0,
  'view_portfolio': 1,
  'view_orders': 2,
  'taken_orders': 3,
  'contacts': 4
};

for (const keyword in keywordsToIndex) {
  if (url.includes(keyword)) {
    const index = keywordsToIndex[keyword];
    header.children[1].children[index].style.color = desiredColor;
    break; // Прерываем цикл, если подходящее ключевое слово найдено
  }
}

