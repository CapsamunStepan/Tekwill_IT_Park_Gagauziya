const header = document.querySelector('header');
const url = window.location.href;
const desiredColor = "#ffc600";
const keywordsToIndex = {
  'news': 0,
  'view_programmers': 1,
  'create_order': 2,
  'view_orders': 3,
  '/order': 3,
  '404': 4
};

for (const keyword in keywordsToIndex) {
  if (url.includes(keyword)) {
    const index = keywordsToIndex[keyword];
    header.children[1].children[index].style.color = desiredColor;
    break; // Прерываем цикл, если подходящее ключевое слово найдено
  }
}

