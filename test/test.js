fetch('http://localhost:8000/v1/1')
    .catch(err => console.log(err))
    .then(response => response.json())
    .then(result => console.log(result))

// let get_user_ID = {login: 'Rubella29', password: 'xxxxxxxxxx'};
let get_user_ID = {login: 'Rubella29', password: 'guygjgjgekhkj'};
    
fetch('http://localhost:8000/v1/auth/login', {method: 'POST', headers: {'Content-Type': 'application/json;charset=utf-8'}, body: JSON.stringify(get_user_ID)})
    .catch(err => console.log(err))
    .then(response => response.json())
    .then(result => console.log(result))


let post_user = {
    "phone": "+79167003020",
    "login": "rubella19",
    "password": "1Qwerty!",
    "name": "Анастасия",
    "birth": "2000-07-28",
    "tg": "@Rubella19",
    "email": "anastasia.a.krasnova@gmail.com"
};

    fetch('http://localhost:8000/v1/auth/register', {method: 'POST', headers: {'Content-Type': 'application/json;charset=utf-8'}, body: JSON.stringify(post_user)})
    .catch(err => console.log(err))
    .then(response => response.json())
    .then(result => console.log(result))



