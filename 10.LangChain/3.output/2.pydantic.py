from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel, Field

load_dotenv()

class MovieReview(BaseModel):
    """ 영화 리뷰 분석 결과 """
    title: str = Field(description="영화 제목")
    sentiment: str = Field(description="감성 분류: 긍정, 부정, 중립")
    score: int = Field(description="1~10 점수")
    summary: str = Field(description="리뷰 요약 (1~2문장)")
    keywords: list[str] = Field(description="핵심 키워드 3개")

llm = ChatOpenAI(model="gpt-4o-mini")

parser = PydanticOutputParser(pydantic_object=MovieReview)
# print("포맷 명령문:")
# print(parser.get_format_instructions())

prompt = ChatPromptTemplate.from_template(
    """ 다음 영화 리뷰를 분석해 주세요. 
리뷰: {review}

{format_instructions}
"""

)

chain = prompt | llm | parser

reviews = [
    'Project Hail Mary우주를 배경으로 한 SF 영화인데, 과학적인 설정과 인간적인 감정선이 정말 잘 어우러졌어요. 긴 러닝타임인데도 몰입감이 좋아서 시간이 금방 지나갑니다. 특히 마지막 장면의 여운이 꽤 오래 남는 영화였어요.',
    'The Mandalorian and Grogu스타워즈 팬이라면 반가운 요소가 많지만, 전체적으로는 이야기의 임팩트가 조금 약하다는 느낌이 있었어요. 액션과 비주얼은 훌륭했지만 예전 시리즈만큼의 압도적인 분위기는 덜했습니다. 그래도 그로구의 귀여움 하나만으로 볼 가치는 충분해요.',
    'Obsession저예산 공포영화인데도 분위기 연출이 상당히 뛰어나서 긴장감이 계속 유지됩니다. 단순히 무섭기만 한 게 아니라 블랙코미디 느낌도 섞여 있어서 색다른 재미가 있어요. 올해 가장 의외의 화제작이라는 말이 괜히 나온 게 아닌 것 같습니다.'
]

for review in reviews:
    result = chain.invoke({
        "review": review,
        "format_instructions": parser.get_format_instructions()
    })

    print(f"제목: {result.title}")
    print(f"감성: {result.sentiment} (점수: {result.score}/10)")
    print(f"요약: {result.summary}")
    print(f"키워드: {result.keywords}")
    print('-' * 30)

    """
    제목: Project Hail Mary
    감성: 긍정 (점수: 9/10)
    요약: SF 영화 'Project Hail Mary'는 과학적 설정과 인간적 감정이 잘 어우러진 작품으로, 몰입감이 뛰어나며 여운이 남는 마지막 장면이 인상적이다.
    키워드: ['SF', '몰입감', '감정선']
    ------------------------------
    제목: The Mandalorian and Grogu
    감성: 중립 (점수: 6/10)
    요약: 스타워즈 팬에게는 반가운 요소가 많지만 이야기의 임팩트가 다소 약하다. 그로구의 귀여움이 큰 장점이다.
    키워드: ['스타워즈', '그로구', '액션']
    ------------------------------
    제목: Obsession
    감성: 긍정 (점수: 8/10)
    요약: 저예산 공포영화임에도 불구하고 뛰어난 분위기 연출과 블랙코미디 요소가 어우러져 긴장감과 색다른 재미를 제공합니다.
    키워드: ['저예산', '공포영화', '블랙코미디']
    ------------------------------
    """