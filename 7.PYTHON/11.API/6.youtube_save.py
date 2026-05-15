# pip install python-dotenv

import csv
import os
import requests
from dotenv import load_dotenv

load_dotenv() # .env 파일을 읽어서 해당 key/value를 메모리(환경변수)에 올려둠

# 환경변수에서 YOUTUBE_API_KEY 값을 읽어옴 (.env는 commit되지 않게 .gitignore에 등록되어 있음)
API_KEY = os.getenv('YOUTUBE_API_KEY')

url = 'https://www.googleapis.com/youtube/v3/search'

search_query = '파이썬 튜토리얼'

params = {
    'part': 'snippet',
    'q': search_query,
    'type': 'video',
    'maxResults': 50,
    'key': API_KEY
}
print('요청 시작')

response = requests.get(url, params)
data = response.json()
print(data)

#csv에 저장
# 인코딩 이모티콘 이모지 절대 사용하지 못하게 할려고
with open('youtube_search_results.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'video_id', 'video_url', 'description']) # 헤더 작성

    for item in data['items']:
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        description = item['snippet']['description']
        
        print(f'제목: {title}, URL: {video_url}, 설명: {description}')
        print('-' * 40)

        writer.writerow([title, video_id, video_url, description])

"""
제목: 최신 파이썬 코딩 무료 강의 | 2024 점프 투 파이썬 통합본, URL: https://www.youtube.com/watch?v=ftQZo7XaTOA, 설명: 점프 투 파이썬과 함께하는 파이썬 입문용 코딩 기초 강의로 프로그래밍을 전혀 모르는 왕초보도 누구나 쉽게 코딩을 배울 수 있도록 ...
----------------------------------------
제목: 파이썬 무료 기초 강의 - 1강 파이썬이란 무엇인가?, URL: https://www.youtube.com/watch?v=yytWGELNeOI, 설명: 점프 투 파이썬과 함께하는 파이썬 입문용 코딩 기초 강의 1강으로 프로그래밍을 전혀 모르는 왕초보도 누구나 쉽게 코딩을 배울 수 ...
----------------------------------------
제목: 파이썬 독학, 제발 설치부터 하지 마세요. (서울대 교수 무료 강의) (1/38), URL: https://www.youtube.com/watch?v=8lCfkW_dIY4, 설명: 
----------------------------------------
제목: 파이썬 무료 강의 100분 완성 (1분 파이썬 모음), URL: https://www.youtube.com/watch?v=T6z-0dpXPvU, 설명: 파이썬 1분 파이썬 모음집입니다. 비전공자도 이해할 수 있도록 실습 대신 이론 위주의 컨텐츠로 구성하여 100분 만에 빠르게 파이썬 ...
----------------------------------------
제목: 파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩], URL: https://www.youtube.com/watch?v=kWiCuklohdY, 설명: 파이썬 무료 강의 (기본편)입니다. 누구나 볼 수 있도록 쉽고 재미있게 제작하였습니다. ^^ 파이썬은 다양한 활용 분야가 있는 인기 ...
----------------------------------------
제목: 코딩 왕초보 탈출 무료 강의 Python 기초 1강 ( by 서울대 교수 ), URL: https://www.youtube.com/watch?v=jrHwm-gNg5Y, 설명: 00:00 Intro 00:34 코딩이란? 03:49 최초의 코드 짜기 07:43 자료형 14:13 기초연산 22:01 요약.
----------------------------------------
제목: 파이썬 당신이 지금 당장 배워야하는 이유 (파이썬 기초), URL: https://www.youtube.com/watch?v=x1VFfTz30VE, 설명: 파이썬기초 #코딩 #프로그래밍 파이썬 기초를 배우면 자동화, 웹 개발, 데이터 분석까지 모두 가능해집니다. 파이썬 기초는 반복 업무 ...
----------------------------------------
제목: 개발자가 보는 프로그래밍 언어좀 해봤다 하는 일반인, URL: https://www.youtube.com/watch?v=59JGaJElY8Y, 설명: 개발 #개발자 #개그 #파이썬 #C언어 #자바.
----------------------------------------
제목: 고수들 github에 나오는 건방진 문법 #python, URL: https://www.youtube.com/watch?v=MeQBuFwdIio, 설명: 
----------------------------------------
제목: 파이썬 코딩 무료 강의 (활용편1) - 추억의 오락실 게임을 만들어 보아요. 3시간이면 충분합니다. [나도코딩], URL: https://www.youtube.com/watch?v=Dkx8Pl6QKW0, 설명: 【신규 강의 안내】 ✨ 챗GPT를 넘어서, 랭체인과 RAG로 만드는 AI 문서 Q&A 챗봇 강의 https://bit.ly/nadoRAG --- 파이썬 무료 ...
----------------------------------------
제목: Python Full Course for Beginners, URL: https://www.youtube.com/watch?v=K5KVEU3aaeQ, 설명: Master Python from scratch No fluff—just clear, practical coding skills to kickstart your journey! Want to dive deeper? - Check ...
----------------------------------------
제목: 파이썬 코딩 기초 강좌 - 파이썬 프로그래밍의 기초, 자료형(2), URL: https://www.youtube.com/watch?v=2FBX-JcZ2ks, 설명: 점프 투 파이썬과 함께하는 파이썬 입문용 코딩 기초 강의 3강으로 프로그래밍을 전혀 모르는 왕초보도 누구나 쉽게 코딩을 배울 수 ...
----------------------------------------
제목: 파이썬 왕초보 기초 강의 완벽 마스터 하는 방법, URL: https://www.youtube.com/watch?v=JE-rdjcNFVQ, 설명: 파이썬으로 자동화 프로그램 만들기 강좌 수강 요령을 담은 파이썬 왕초보 기초 강의 완벽 마스터 하는 방법을 공유해봅니다.
----------------------------------------
제목: Learn Python for FREE in 2025, URL: https://www.youtube.com/watch?v=q2-pnQffZik, 설명: Learn Python for FREE in 2025 #coding #compsci #python #fyp Source: TikTok (individualkex)
----------------------------------------
제목: Python Syllabus | Python for Beginners | Complete Python Course #pythonlearning, URL: https://www.youtube.com/watch?v=WCM65ION4nE, 설명: Learn Python for free from this own pace learning platform https://cramming.arlarse.tech/c/python-for-beginner #python ...
----------------------------------------
제목: Python Full Course for Beginners, URL: https://www.youtube.com/watch?v=_uQrJ0TkZlc, 설명: Learn Python for AI, machine learning, and web development with this beginner-friendly course! Get 6 months of PyCharm ...
----------------------------------------
제목: python programming|python for beginners|python full course, URL: https://www.youtube.com/watch?v=80yIVH2aOy0, 설명: python programming|python for beginners|python full course @monuinstitute python tutorial, learn python, python basics, ...
----------------------------------------
제목: Why This Turtle Graphics Python Tutorial is Worth Your Time, URL: https://www.youtube.com/watch?v=tSZc6Mvqt78, 설명: Why This Turtle Graphics Python Tutorial is Worth Your Time @monuinstitute Some of you asked me about Python courses for ...
----------------------------------------
제목: Learn Python in Only 30 Minutes (Beginner Tutorial), URL: https://www.youtube.com/watch?v=Ro_MScTDfU4, 설명: In this video I'm going to be teaching you the core concepts that you need to know to get started with using Python. ▷ Become ...
----------------------------------------
제목: Impress your crush using Python Code ❤️, URL: https://www.youtube.com/watch?v=fXxUYb0s-pc, 설명: Code with explanation is here: https://aitoolz.ai/impress-your-crush-using-python-code/
----------------------------------------
제목: [1분 파이썬] 2강 연산자(1)_교재제공, URL: https://www.youtube.com/watch?v=zpW543qFsU4, 설명: 교재 다운로드- https://blog.naver.com/conding_1_bite #파이썬 #python #강의 #코딩 #교재 #연산자.
----------------------------------------
제목: Amazing Flower Design using Python turtle 🐢 #python #coding #funny #viral #trending #design, URL: https://www.youtube.com/watch?v=W-8j4MrsX2s, 설명: Python Projects for Begineers Python Turtle Programming with Turtle Turtle Graphics Drawing with Python Turtle Python Turtle ...
----------------------------------------
제목: Python for Beginners - Learn Coding with Python in 1 Hour, URL: https://www.youtube.com/watch?v=kqtD5dpn9C8, 설명: Learn Python basics in just 1 hour! Perfect for beginners interested in AI and coding. ⚡ Plus, get 6 months of PyCharm FREE with ...
----------------------------------------
제목: Python Roadmap for Beginners! 🐍 Learn Python Programming Step-by-Step&quot; #python #conding, URL: https://www.youtube.com/watch?v=IfKlGhRc7Dc, 설명: Python Roadmap for Beginners! Learn Python Programming Step-by-Step" @MissionAdda4 #codingtutorial #pythonroadmap ...
----------------------------------------
제목: How to draw a triangle using turtle in Python, URL: https://www.youtube.com/watch?v=hxgVtGGegC8, 설명: shorts #Python How to draw a triangle using turtle in Python!
----------------------------------------
제목: Python Basics: Your FIRST Program in Under a Minute! 🚀, URL: https://www.youtube.com/watch?v=nluUYtejoIE, 설명: In this quick tutorial, I'll show you how to write your very first line of Python code: the classic "Hello, World!" ✨ Whether you're a ...
----------------------------------------
제목: 👩‍💻 Python for Beginners Tutorial, URL: https://www.youtube.com/watch?v=b093aqAZiPU, 설명: In this step-by-step Python for beginner's tutorial, learn how you can get started programming in Python. In this video, I assume ...
----------------------------------------
제목: Python Full Course for free 🐍, URL: https://www.youtube.com/watch?v=ix9cRaBkVe0, 설명: python #tutorial #beginners Python tutorial for beginners' full course 2024 *Learn Python in 1 HOUR* ...
----------------------------------------
제목: Python Tutorial for Beginners - Learn Python in 5 Hours [FULL COURSE], URL: https://www.youtube.com/watch?v=t8pPdKYpowI, 설명: Grab your free IT Fundamentals Roadmap: https://bit.ly/3GV5Noy Hands-On course to learn the complete SDLC - from code to ...
----------------------------------------
제목: Python Basics: The Best Way to Learn Python Programming (2024), URL: https://www.youtube.com/watch?v=GfWRxr1OBm4, 설명: Python Basics: The Best Way to Learn Python Programming (2024) @monuinstitute Some of you asked me about Python ...
----------------------------------------
제목: How I Would Learn Python FAST (if I could start over), URL: https://www.youtube.com/watch?v=mC4nyib2sfg, 설명: If I had to learn Python again from scratch.. and learn it FAST - this is exactly how I'd do it. After teaching myself Python in just two ...
----------------------------------------
제목: Apprendre Python en 1 heure - Cours Complet Débutant (4K), URL: https://www.youtube.com/watch?v=5EnpNI2iCZA, 설명: RÉCUPÈRE TON KIT DE SURVIE PYTHON (PDF + EXERCICES) : https://www.commentcoder.com/kit/python/ PASSE AU ...
----------------------------------------
제목: Learn Python in Less than 10 Minutes for Beginners (Fast &amp; Easy), URL: https://www.youtube.com/watch?v=fWjsdhR3z3c, 설명: In this crash course I'll be teaching you the basics of Python in less than 10 minutes. Python is super easy to learn compared to ...
----------------------------------------
제목: Junior vs senior python developer 🐍 | #python #coding #programming #shorts  @Codingknowledge-yt, URL: https://www.youtube.com/watch?v=Mf9GCn_LsUI, 설명: Junior vs senior python developer | #python #coding #javascript #programming @Codingknowledge-yt @Codingknowledge-yt ...
----------------------------------------
제목: Start coding with PYTHON in 5 minutes! 🐍, URL: https://www.youtube.com/watch?v=Sg4GMVMdOPo, 설명: python #pythontutorial #pythoncourse This is the introductory video to my new FREE 12 Hour Python course. There is an ...
----------------------------------------
제목: Top 10 Most Important Python Functions You Must Know! 🚀 | Python Tutorial for Beginners, URL: https://www.youtube.com/watch?v=gbYLsUngzLc, 설명: In this video, we'll explore the most important Python functions every beginner and intermediate programmer must know! From ...
----------------------------------------
제목: Python AI And Generative AI Course For Beginners #ai #python #tutorial #course #study #learning, URL: https://www.youtube.com/watch?v=LRhOzoxHlJo, 설명: Python AI And Generative AI Course For Beginners Your Queries :- Learn AI basics with python Generative ai essential full course ...
----------------------------------------
제목: How to visualize data with Python in Excel. 🤯 #excel  #python #tutorial, URL: https://www.youtube.com/watch?v=EmxXYzX6iEs, 설명: 
----------------------------------------
제목: Programming#python#javascript#java#c++#assembly #coding, URL: https://www.youtube.com/watch?v=CMzbwSi8_q8, 설명: 
----------------------------------------
제목: Learn Python - Full Course for Beginners [Tutorial], URL: https://www.youtube.com/watch?v=rfscVS0vtbw, 설명: This course will give you a full introduction into all of the core concepts in python. Follow along with the videos and you'll be a ...
----------------------------------------
제목: How To Call API In Python, URL: https://www.youtube.com/watch?v=0_zphmXBiZs, 설명: In this video I will showing you how to Call API in Python if f you know than subscribe the channel and press the thumbs up button ...
----------------------------------------
제목: Python LAMBDA FUNCTION?! #python #programming #coding, URL: https://www.youtube.com/watch?v=ss-I6WAiMFA, 설명: This video shows a quick illustration of what lambda functions are in Python. These are also referred to as anonymous functions.
----------------------------------------
제목: How to create a virus using python🦠, URL: https://www.youtube.com/watch?v=c0MNpou4zOA, 설명: Discover the intricacies of malware creation with Python in this comprehensive guide. Learn how to develop viruses, understand ...
----------------------------------------
제목: Python Programming - A Full Course for Beginners (Learn Python in 2025!), URL: https://www.youtube.com/watch?v=Wghz6w0btxI, 설명: Python Programming - A Full Course for Beginners (Learn Python in 2025!) @monuinstitute Some of you asked me about Python ...
----------------------------------------
제목: Learn Python in 1 hour! 🐍, URL: https://www.youtube.com/watch?v=8KCuHHeC_M0, 설명: python #pythontutorial #pythoncourse This is a quick introduction to the Python programming language. If you would like to learn ...
----------------------------------------
제목: Pygame - Display Image in Pygame python || Pygame python tutorial #python #pygame, URL: https://www.youtube.com/watch?v=dZ8VrmzYL2A, 설명: Pygame - Display image pygame in python || How to make game using python #shorts #trending #tutorials #python ...
----------------------------------------
제목: Python pygame Tutorial #python #pygame #coding #programming, URL: https://www.youtube.com/watch?v=UByzZYqOHPY, 설명: 
----------------------------------------
제목: Do THIS instead of watching endless tutorials - how I’d learn Python FAST…, URL: https://www.youtube.com/watch?v=mB0EBW-vDSQ, 설명: These are two of the best beginner-friendly Python resources I recommend: Python Programming Fundamentals (Datacamp) ...
----------------------------------------
제목: Python in Excel - Beginner Tutorial, URL: https://www.youtube.com/watch?v=qEwnlMBaLfc, 설명: Learn Excel in just 2 hours: https://kevinstratvert.thinkific.com In this step-by-step tutorial, learn how you can use Python in ...
----------------------------------------
제목: Python courses for Beginners (FREE), URL: https://www.youtube.com/watch?v=vMV1s-1BKvc, 설명: 
----------------------------------------
"""