# 외부 모듈은 pip install requset 로 설치한다.
# 그러면, pypi.org로 부터 다운로드 받아서, 나의 "가상환경"에 설치가 됨
import requests

# 외부에 HTTP 요청을 대신 해주는 라이브러리
# resp = requests.get("http://www.example.com")
# print(resp)
# print(resp.status_code)
# print(resp.headers)
# print("웹 페이지 내용: ", resp.text)

resp = requests.get('https://api.github.com')
if (resp.status_code == 200):
    print(resp.text)
else:
    print("해당 페이지를 가져오는데 실패했습니다. code: ", resp.status_code)
    
"""
# <Response [200]>
# 200
# {'Date': 'Mon, 11 May 2026 08:14:54 GMT', 'Content-Type': 'text/html', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Server': 'cloudflare', 'Last-Modified': 'Sat, 09 May 2026 09:00:11 GMT', 'Allow': 'GET, HEAD', 'cf-cache-status': 'HIT', 'Age': '6620', 'Content-Encoding': 'gzip', 'CF-RAY': '9f9fbb991ee429dd-FUK'}
# 웹 페이지 내용:  <!doctype html><html lang="en"><head><title>Example Domain</title><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{background:#eee;width:60vw;margin:15vh auto;font-family:system-ui,sans-serif}h1{font-size:1.5em}div{opacity:0.8}a:link,a:visited{color:#348}</style></head><body><div><h1>Example Domain</h1><p>This domain is for use in documentation examples without needing permission. Avoid use in operations.</p><p><a href="https://iana.org/domains/example">Learn more</a></p></div></body></html>
"""