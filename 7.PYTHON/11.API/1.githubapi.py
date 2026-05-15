import requests

url = 'https://api.github.com/users/shimjeongho/repos'

resp = requests.get(url)
repos = resp.json()

# print(repos)
# 리스트 배열로 나타남
# [{}, {}, {}, {}]

# print(data)
data = []

for repo in repos:
    name = repo['name']
    html_url = repo['html_url']
    description = repo['description']
    data.append({'name': name, 'html_url': html_url, 'desc': description})

print(f"{'리포이름' : <30} {'리포URL' : <50} {'설명' :<20}")
for d in data:
    print(f"{d['name']:<30} {d['html_url']:<50}")

"""
리포이름                           리포URL                                              설명                  
bookhub                        https://github.com/shimjeongho/bookhub            
Credit_Card_Fraud_Detection    https://github.com/shimjeongho/Credit_Card_Fraud_Detection
ebook-viewer                   https://github.com/shimjeongho/ebook-viewer       
group-project                  https://github.com/shimjeongho/group-project      
spc2026                        https://github.com/shimjeongho/spc2026            
spring-boot-app1               https://github.com/shimjeongho/spring-boot-app1   
study.doc                      https://github.com/shimjeongho/study.doc     
"""