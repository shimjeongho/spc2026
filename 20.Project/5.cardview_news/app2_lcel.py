# pip install lxml
import base64, requests
from bs4 import BeautifulSoup

from dotenv import load_dotenv

from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
client = OpenAI()


def fetch_news(query):
    """뉴스 검색 결과를 가져온다."""
    url = "https://news.google.com/rss/search"
    params = {
        "q": query,
        "hl": "ko",
        "gl": "KR",
        "ceid": "KR:ko"
    }

    xml = requests.get(url, params=params, timeout=10).text
    soup = BeautifulSoup(xml, "xml")

    items = []
    for item in soup.find_all("item")[:8]:
        items.append({
            "title": item.title.text,
            "link": item.link.text,
            "date": item.pubDate.text
        })
    return str(items)

def make_image_prompt(news):
    prompt = f"""
다음 뉴스 내용을 바탕으로 웹툰형 카드뉴스 이미지 생성 프롬프트를 만드시오.

조건:
- 한 장짜리 이미지
- 여러 컷 웹툰 스타일
- 한국어 텍스트 포함
- 날짜가 있다면, 각 날짜별로 패널을 구성
- 뉴스 카드 + 만화 컷 + 인포그래픽 형태로 혼합 구성
- 인물은 실제 해당 유명인을 캐릭터화 한 느낌으로 생성
- 회사 로고나 상표 등을 적절하게 활용해서 실제 내용을 살림

뉴스:
{news}
"""
    
    result = llm.invoke(prompt)
    return result.content


def generate_image(image_prompt, output="output.png"):
    result = client.images.generate(
        model="gpt-image-1.5",
        prompt=image_prompt,
        size="1024x1536",
        quality="medium"
    )

    image_base64 = result.data[0].b64_json
    with open(output, "wb") as f:
        f.write(base64.b64decode(image_base64))

news_agent = create_agent(
    model=llm,
    tools=[fetch_news],
    system_prompt="""
너는 뉴스 조사 에이전트야
사용자 주제와 관련된 뉴스 목록을 수집하고, 일정/날짜/행사/만남 정보를
중심으로 정리한다.
"""
)


summarize_chain = {
    ChatPromptTemplate.from_messages([
        ("system", "너는 OOO 이다...")
        ("human", "다음 뉴스로 OOO 해라.")
    ])
    | llm
    | StrOutputParser()
}

pipeline = (
    RunnablePassthrough.assign(news=fetch_news)
    | RunnablePassthrough.assign(summary=summarize_chain)
    | RunnablePassthrough.assign(image_prompt=image_prompt)
    | RunnablePassthrough.assign(image_path=generate_image)
)
def main():
    

    # 1. 뉴스 수집
    result = pipeline.invoke({"query": "젠슨 황 4박 5일 한국 방문 일정"})
    print("\n[뉴스 요약]")
    print(result['summary'])
    print('-' * 60)

    # 2. 뉴스 요약 및 이미지 생성 프롤프트
    images_prompt = make_image_prompt(result)
    print("\n[이미지 프롬프트]")
    print(images_prompt)

    # 3. 이미지 생성
    output_file = generate_image(images_prompt)
    print(f"\n이미지 생성 완료: {output_file}")

if __name__ == "__main__":
    main()
    
"""
[뉴스 요약]
현재 젠슽 황의 한국 방문 일정에 대한 구체적인 뉴스는 확인되지 않았습니다. 최신 정보를 원하신다면, 이후 뉴스 업데이트를 추적하거나 관련 공식 발표를 확인할 필요가 있습니다. 추가로 다른 주제에 대한 뉴스가 필요하신 경우 언제든지 말씀해 주세요.
------------------------------------------------------------

[이미지 프롬프트]
### 이미지 생성 프롬프트

- **스타일**: 웹툰 형식의 카드뉴스
- **구성**: 한 장의 이미지에 여러 컷으로 나누어 구성
- **텍스트**: 한국어 텍스트 포함

---

1. **컷 1**: 상단
   - **배경**: 흐릿한 도심의 랜드마크 (예: 서울타워)
   - **내용**: "젠슽 황, 한국 방문 일정 불확실!" (큰 글씨로 중앙 배치)

2. **컷 2**: 중간 왼쪽
   - **캐릭터**: 젠슽 황의 캐릭터화된 모습, 놀란 표정
   - **대사**: "방문 일정이 확인되지 않았다니, 무슨 일이죠?"

3. **컷 3**: 중간 오른쪽
   - **배경**: 뉴스 배경 (예: 뉴스 스튜디오)
   - **캐릭터**: 뉴스 진행자가 서 있는 모습
   - **대사**: "최신 정보는 공식 발표를 통해 확인하세요!"

4. **컷 4**: 하단
   - **인포그래픽**: 뉴스 업데이트 방법
   - **내용**: "뉴스 업데이트 추적하기"
     - 방법 아이콘: 웹사이트, SNS, 뉴스앱 등 아이콘 표시
   - **텍스트**: "더 궁금한 점이 있다면, 언제든지 말씀해 주세요!"

5. **로고 및 상표**: 이미지 구석에 관련 공식 뉴스 매체 로고 삽입.

---

위의 프롬프트를 바탕으로 웹툰 스타일의 카드뉴스 이미지를 생성해주세요.

이미지 생성 완료: None                                   //// ######### 파일명을 안 넣어서 None으로 나옴 이미지는 생성 완료

"""