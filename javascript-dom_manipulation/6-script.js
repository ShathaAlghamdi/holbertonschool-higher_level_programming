// fetch returns a Promise: wait for the response, read it as JSON, then use it
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    document.querySelector('#character').textContent = data.name;
  });
