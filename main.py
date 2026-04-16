

users: list = [
    {'username': 'oliwia', 'location':'łódź','posts':1,'usermessage':['życzenia1','kocham legie','sprzedam opla','kiwi']},
    {'username': 'paweł', 'location':'ostróda','posts':2,'usermessage':['życzenia2','kocham legie','sprzedam opla',]},
    {'username': 'eliza', 'location':'radom','posts':3,'usermessage':['życzenia3','kocham legie','sprzedam opla',]},
    {'username': 'eliza', 'location': 'dęblin', 'posts': 4, 'usermessage': ['życzenia4','kocham legie','sprzedam opla',]},
]

for user in users:

    print(f'twój znajomy {user['username']} z miejscowości {user["location"]} opublikował {user['posts']} wiadomości. Ostatnia wiadomość {user['usermessage']}')
#     Twój znajomy filip z miejscowości dęblin opublikował 1 post o treści: życzenia
