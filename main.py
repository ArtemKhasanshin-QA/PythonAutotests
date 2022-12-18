import requests
import json

token = '99f9542ab0cf00c08d6e7b2497e009eb'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": 'Красавчик',
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})
print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 2435,
    "name": "Вау",
    "photo": ""
})

print(response_put.text)