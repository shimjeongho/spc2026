from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://news.naver.com/section/105")

    headlines = page.locator(".section_article.as_headline a.sa_text_title")
    print("헤드라인 갯수: ", headlines.count())
    for i in range(headlines.count()):
        news = headlines.nth(i)

        # 제목 가져오기
        title = news.inner_text().strip()

        # 링크 가져오기
        href = news.get_attribute('href')

        print(f"{i+1}. {title}\n   {href}")

    input("엔터")

    """
    (py312) C:\src\SPC2026\7.PYTHON\6.scrap>python 5.playwright_naver.py
    헤드라인 갯수:  8
    1. SK AX, 오픈AI와 협력…고성능 AX 환경 만든다
    https://n.news.naver.com/mnews/article/374/0000510034
    2. "등본 발급해줘"…카카오, 'AI 국민비서'에 음성 기능 추가
    https://n.news.naver.com/mnews/article/018/0006280722
    3. 해커에 뚫려 개인정보 2만7천건 유출…보람상조 7곳에 과징금 5.4억원
    https://n.news.naver.com/mnews/article/374/0000510079
    4. 삼성 헬스, '천만 러너' 잡는다…데이터 러닝 강화
    https://n.news.naver.com/mnews/article/001/0016076648
    5. 네이버에서 외부 포인트 쌓고 할인쿠폰도 다운된다
    https://n.news.naver.com/mnews/article/009/0005679768
    6. SKT, 유심 안전조치 강화…개보위 "추가 이행점검"
    https://n.news.naver.com/mnews/article/001/0016076593
    7. AI 컨트롤타워 공백 우려에...배경훈 부총리, 국가AI전략위까지 총괄
    https://n.news.naver.com/mnews/article/011/0004620703
    8. AI가 해킹하는 시대인데…중소기업 대응 착수까지 106일[AI픽]
    https://n.news.naver.com/mnews/article/001/0016076118
    엔터
    """