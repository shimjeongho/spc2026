# pip install python-dotenv

import os
import requests
from dotenv import load_dotenv

load_dotenv() # .env 파일을 읽어서 해당 key/value를 메모리(환경변수)에 올려둠

# 환경변수에서 YOUTUBE_API_KEY 값을 읽어옴 (.env는 commit되지 않게 .gitignore에 등록되어 있음)
API_KEY = os.getenv('YOUTUBE_API_KEY')

search_url = 'https://www.googleapis.com/youtube/v3/search'
video_api_url = 'https://www.googleapis.com/youtube/v3/videos'

# 검색어
search_query = "파이썬 튜토리얼"

# Search API 요청 파라미터
search_params = {
    'part': 'snippet',
    'q': search_query,
    'type': 'video',
    'maxResults': 50,
    'key': API_KEY
}

# 검색 요청
response = requests.get(search_url, params=search_params)

# JSON 변환
data = response.json()

# 검색 결과 저장
search_results = data['items']

# 최종 결과 저장용
table = []

# 가져오고 싶은 추가정보
table_header = ['index', 'title', 'view_count', 'video_url']

# 각 영상 상세 조회
for index, result in enumerate(search_results, start=1):

    # 제목
    title = result['snippet']['title']

    # 비디오 ID
    video_id = result['id']['videoId']

    # 실제 유튜브 URL
    youtube_watch_url = f'https://www.youtube.com/watch?v={video_id}'

   # videos API 요청 파라미터
    video_params = {
        'part': 'statistics',
        'id': video_id,
        'key': API_KEY
    }

     # videos API 호출
    video_response = requests.get(
        video_api_url,
        params=video_params
    )

    print(video_response)

    # JSON 데이터 변환
    video_data = video_response.json()
    
    # 조회수 추출
    if 'items' in video_data and video_data['items']:
        view_count = video_data['items'][0]['statistics']['viewCount']
    else:
        view_count = 'N/A'

    # 테이블 저장
    table.append([index, title, view_count, youtube_watch_url])

# 출력
print(table_header)

for row in table:
    print(row)

"""
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
['index', 'title', 'view_count', 'video_url']
[1, '최신 파이썬 코딩 무료 강의 | 2024 점프 투 파이썬 통합본', '569828', 'https://www.youtube.com/watch?v=ftQZo7XaTOA']
[2, '파이썬 무료 기초 강의 - 1강 파이썬이란 무엇인가?', '831936', 'https://www.youtube.com/watch?v=yytWGELNeOI']
[3, '파이썬 독학, 제발 설치부터 하지 마세요. (서울대 교수 무료 강의) (1/38)', '5393', 'https://www.youtube.com/watch?v=8lCfkW_dIY4']
[4, '파이썬 무료 강의 100분 완성 (1분 파이썬 모음)', '764970', 'https://www.youtube.com/watch?v=T6z-0dpXPvU']
[5, '파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]', '5835986', 'https://www.youtube.com/watch?v=kWiCuklohdY']
[6, '코딩 왕초보 탈출 무료 강의 Python 기초 1강 ( by 서울대 교수 )', '17169', 'https://www.youtube.com/watch?v=jrHwm-gNg5Y']
[7, '파이썬 당신이 지금 당장 배워야하는 이유 (파이썬 기초)', '8504', 'https://www.youtube.com/watch?v=x1VFfTz30VE']
[8, '개발자가 보는 프로그래밍 언어좀 해봤다 하는 일반인', '1040375', 'https://www.youtube.com/watch?v=59JGaJElY8Y']
[9, '고수들 github에 나오는 건방진 문법 #python', '274546', 'https://www.youtube.com/watch?v=MeQBuFwdIio']
[10, '파이썬 코딩 무료 강의 (활용편1) - 추억의 오락실 게임을 만들어 보아요. 3시간이면 충분합니다. [나도코딩]', '3030227', 'https://www.youtube.com/watch?v=Dkx8Pl6QKW0']
[11, 'Python Full Course for Beginners', '6274390', 'https://www.youtube.com/watch?v=K5KVEU3aaeQ']
[12, '파이썬 코딩 기초 강좌 - 파이썬 프로그래밍의 기초, 자료형(2)', '143765', 'https://www.youtube.com/watch?v=2FBX-JcZ2ks']
[13, '파이썬 왕초보 기초 강의 완벽 마스터 하는 방법', '798', 'https://www.youtube.com/watch?v=JE-rdjcNFVQ']
[14, 'Learn Python for FREE in 2025', '1097954', 'https://www.youtube.com/watch?v=q2-pnQffZik']
[15, 'Python Syllabus | Python for Beginners | Complete Python Course #pythonlearning', '1031446', 'https://www.youtube.com/watch?v=WCM65ION4nE']
[16, 'Python Full Course for Beginners', '47690226', 'https://www.youtube.com/watch?v=_uQrJ0TkZlc']
[17, 'python programming|python for beginners|python full course', '1285082', 'https://www.youtube.com/watch?v=80yIVH2aOy0']
[18, 'Why This Turtle Graphics Python Tutorial is Worth Your Time', '107985', 'https://www.youtube.com/watch?v=tSZc6Mvqt78']
[19, 'Learn Python in Only 30 Minutes (Beginner Tutorial)', '752074', 'https://www.youtube.com/watch?v=Ro_MScTDfU4']
[20, 'Impress your crush using Python Code ❤️', '2537810', 'https://www.youtube.com/watch?v=fXxUYb0s-pc']
[21, '[1분 파이썬] 2강 연산자(1)_교재제공', '10423', 'https://www.youtube.com/watch?v=zpW543qFsU4']
[22, 'Amazing Flower Design using Python turtle 🐢 #python #coding #funny #viral #trending #design', '1607005', 'https://www.youtube.com/watch?v=W-8j4MrsX2s']
[23, 'Python for Beginners - Learn Coding with Python in 1 Hour', '24237470', 'https://www.youtube.com/watch?v=kqtD5dpn9C8']
[24, 'Python Roadmap for Beginners! 🐍 Learn Python Programming Step-by-Step&quot; #python #conding', '2827581', 'https://www.youtube.com/watch?v=IfKlGhRc7Dc']
[25, 'How to draw a triangle using turtle in Python', '203852', 'https://www.youtube.com/watch?v=hxgVtGGegC8']
[26, 'Python Basics: Your FIRST Program in Under a Minute! 🚀', '1200586', 'https://www.youtube.com/watch?v=nluUYtejoIE']
[27, '👩\u200d💻 Python for Beginners Tutorial', '4440664', 'https://www.youtube.com/watch?v=b093aqAZiPU']
[28, 'Python Tutorial for Beginners - Learn Python in 5 Hours [FULL COURSE]', '6739287', 'https://www.youtube.com/watch?v=t8pPdKYpowI']
[29, 'Python Full Course for free 🐍', '9768868', 'https://www.youtube.com/watch?v=ix9cRaBkVe0']
[30, 'Python Basics: The Best Way to Learn Python Programming (2024)', '2347026', 'https://www.youtube.com/watch?v=GfWRxr1OBm4']
[31, 'How I Would Learn Python FAST (if I could start over)', '442836', 'https://www.youtube.com/watch?v=mC4nyib2sfg']
[32, 'Apprendre Python en 1 heure - Cours Complet Débutant (4K)', '518189', 'https://www.youtube.com/watch?v=5EnpNI2iCZA']
[33, 'Learn Python in Less than 10 Minutes for Beginners (Fast &amp; Easy)', '1413015', 'https://www.youtube.com/watch?v=fWjsdhR3z3c']
[34, 'Start coding with PYTHON in 5 minutes! 🐍', '740899', 'https://www.youtube.com/watch?v=Sg4GMVMdOPo']
[35, 'Junior vs senior python developer 🐍 | #python #coding #programming #shorts  @Codingknowledge-yt', '2586741', 'https://www.youtube.com/watch?v=Mf9GCn_LsUI']
[36, 'Top 10 Most Important Python Functions You Must Know! 🚀 | Python Tutorial for Beginners', '213706', 'https://www.youtube.com/watch?v=gbYLsUngzLc']
[37, 'Python AI And Generative AI Course For Beginners #ai #python #tutorial #course #study #learning', '349477', 'https://www.youtube.com/watch?v=LRhOzoxHlJo']
[38, 'How to visualize data with Python in Excel. 🤯 #excel  #python #tutorial', '101020', 'https://www.youtube.com/watch?v=EmxXYzX6iEs']
[39, 'Programming#python#javascript#java#c++#assembly #coding', '785525', 'https://www.youtube.com/watch?v=CMzbwSi8_q8']
[40, 'Learn Python - Full Course for Beginners [Tutorial]', '48730007', 'https://www.youtube.com/watch?v=rfscVS0vtbw']
[41, 'How To Call API In Python', '103127', 'https://www.youtube.com/watch?v=0_zphmXBiZs']
[42, 'Python LAMBDA FUNCTION?! #python #programming #coding', '2766072', 'https://www.youtube.com/watch?v=ss-I6WAiMFA']
[43, 'How to create a virus using python🦠', '1503417', 'https://www.youtube.com/watch?v=c0MNpou4zOA']
[44, 'Python Programming - A Full Course for Beginners (Learn Python in 2025!)', '128014', 'https://www.youtube.com/watch?v=Wghz6w0btxI']
[45, 'Learn Python in 1 hour! 🐍', '562915', 'https://www.youtube.com/watch?v=8KCuHHeC_M0']
[46, 'Python pygame Tutorial #python #pygame #coding #programming', '427530', 'https://www.youtube.com/watch?v=UByzZYqOHPY']
[47, 'Pygame - Display Image in Pygame python || Pygame python tutorial #python #pygame', '1154597', 'https://www.youtube.com/watch?v=dZ8VrmzYL2A']
[48, 'Do THIS instead of watching endless tutorials - how I’d learn Python FAST…', '597644', 'https://www.youtube.com/watch?v=mB0EBW-vDSQ']
[49, 'Python lernen | 1h Tutorial für Anfänger (deutsch)', '111800', 'https://www.youtube.com/watch?v=loXS62zXmrk']
[50, 'Python in Excel - Beginner Tutorial', '567384', 'https://www.youtube.com/watch?v=qEwnlMBaLfc']
"""