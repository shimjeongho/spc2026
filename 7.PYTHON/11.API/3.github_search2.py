import requests

url = 'https://api.github.com/search/repositories'

keyword = "chatbot"

max_page = 10
per_page = 100

all_repos = []

for page in range(1, max_page + 1):
    params = {
        'q': keyword,
        'per_page': per_page,
        'page': page
    }

    resp = requests.get(url, params)
    print('요청 성공 여부: ', resp.status_code == 200)
    data = resp.json()

# print(data)

    if 'items' in data:
        repos = data['items']
        for repo in repos:
            name = repo['name']
            full_name = repo['full_name']
            html_url = repo['html_url']
            desc = repo['description']
            all_repos.append({'name': name, 'full_name': full_name, 'url': html_url, 'description': desc})

print(all_repos)
        # print(f'리포명: {name}, 풀네임: {full_name}, URL: {html_url}, 설명: {desc}')


"""
[{'name': 'vk-markovify-chatbot', 'full_name': 'monosans/vk-markovify-chatbot', 'url': 'https://github.com/monosans/vk-markovify-chatbot', 'description': 'Бот для ВКонтакте, генерирующий сообщения Марковским процессом на основе сообщений из чата. Witless и сглыпа на минималках.'}, 
 {'name': 'Restaurant-chatbot', 'full_name': 'AindriyaBarua/Restaurant-chatbot', 'url': 'https://github.com/AindriyaBarua/Restaurant-chatbot', 'description': 'Tutorial to make a simple NLP chatbot with Intent classification, FastText, Flask, AJAX'},
 {'name': 'python-twitch-chatbot', 'full_name': 'MitchellHarrison/python-twitch-chatbot', 'url': 'https://github.com/MitchellHarrison/python-twitch-chatbot', 'description': 'A custom, 100% Python Twitch Chatbot that stores chat/viewership data in a PostgreSQL database.'},
 {'name': 'megahal', 'full_name': 'kranzky/megahal', 'url': 'https://github.com/kranzky/megahal', 'description': 'MegaHAL is a learning chatterbot.'}, 
 {'name': 'RasaGPT', 'full_name': 'paulpierre/RasaGPT', 'url': 'https://github.com/paulpierre/RasaGPT', 'description': '💬 RasaGPT is the first headless LLM chatbot platform built on top of Rasa and Langchain. Built w/ Rasa, FastAPI, Langchain, LlamaIndex, SQLModel, pgvector, ngrok, telegram'},
 {'name': 'AwesomeBot', 'full_name': 'progdisc/AwesomeBot', 'url': 'https://github.com/progdisc/AwesomeBot', 'description': 'chatbot for /r/learnprogramming (un)offical discord channel'},
 {'name': 'kaggle-lmsys-chatbot-arena', 'full_name': 'tascj/kaggle-lmsys-chatbot-arena', 'url': 'https://github.com/tascj/kaggle-lmsys-chatbot-arena', 'description': 'Solution of Kaggle competition: LMSYS - Chatbot Arena Human Preference Predictions'}
 ...]
"""