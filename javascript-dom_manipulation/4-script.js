// Create a new <li>Item</li> and append it to ul.my_list on each click
document.querySelector('#add_item').addEventListener('click', function () {
  const li = document.createElement('li');
  li.textContent = 'Item';
  document.querySelector('.my_list').appendChild(li);
});
