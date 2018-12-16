import os
from tinydb import TinyDB, Query

path_db = './loggathon/db.json'
os.remove(path_db)
open(path_db, 'a').close()
db = TinyDB(path_db)

users_data = [
    {
        'name': 'Loja A',
        'email': 'lojaa@gmail.com',
        'address': 'Alameda Santos',
        'number': 2400,
        'neighborhood': 'Jardim Paulista',
        'city': 'São Paulo',
        'state': 'SP',
        'cep': '01418-200',
        'password': 'password'
    },
    {
        'name': 'Loja B',
        'email': 'lojab@gmail.com',
        'address': 'Rua Bela Cintra',
        'number': 2500,
        'neighborhood': 'Jardim Paulista',
        'city': 'São Paulo',
        'state': 'SP',
        'cep': '01418-200',
        'password': 'password'
    },
    {
        'name': 'Loja C',
        'email': 'lojac@gmail.com',
        'address': 'Rua Haddock Lobo',
        'number': 2600,
        'neighborhood': 'Jardim Paulista',
        'city': 'São Paulo',
        'state': 'SP',
        'cep': '01418-200',
        'password': 'password'
    },
    {
        'name': 'Loja D',
        'email': 'lojad@gmail.com',
        'address': 'Av. Paulista',
        'number': 100,
        'neighborhood': 'Jardim Paulista',
        'city': 'São Paulo',
        'state': 'SP',
        'cep': '01418-200',
        'password': 'password'
    }
]

sells_data = [
    {
        'store': 'lojaa@gmail.com',
        'sells': [
            {
                'title': 'HD Externo',
                'status': 'Não recolhido',
                'volume': '20cm x 15cm x 5 cm',
                'weight': 0.8,
                'sell_date': int(1544923966.623495),
                'image': 'f4ed888d_hd_externo.jpg'
            },
        ]
    },
    {
        'store': 'lojab@gmail.com',
        'sells': [
            {
                'title': 'HD Externo',
                'status': 'Não recolhido',
                'volume': '20cm x 15cm x 5 cm',
                'weight': 0.8,
                'sell_date': int(1544923966.623495),
                'image': 'f4ed888d_hd_externo.jpg'
            },
        ]
    },
    {
        'store': 'lojac@gmail.com',
        'sells': [
            {
                'title': 'HD Externo',
                'status': 'Não recolhido',
                'volume': '20cm x 15cm x 5 cm',
                'weight': 0.8,
                'sell_date': int(1544923966.623495),
                'image': 'f4ed888d_hd_externo.jpg'
            },
        ]
    },
    {
        'store': 'lojad@gmail.com',
        'sells': [
            {
                'title': 'HD Externo',
                'status': 'Não recolhido',
                'volume': '20cm x 15cm x 5 cm',
                'weight': 0.8,
                'sell_date': int(1544923966.623495),
                'image': 'f4ed888d_hd_externo.jpg'
            },
        ]
    }
]

users_table = db.table('users')
sells_table = db.table('sells')
users_table.insert_multiple(users_data)
sells_table.insert_multiple(sells_data)
