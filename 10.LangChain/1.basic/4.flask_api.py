from flask import Flask, request, jsonify
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI    
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

app = Flask(__name__)
llm = ChatOpenAI(model='gpt-4o-mini')

@app.route('/api/name')
def name():
    prompt = [
        SystemMessage(content="You are a creative branding expert."),
        HumanMessage(content="What's a good company name that makes computer games. Do not give any explanation. Just give me the naems."),
    ]
    result = llm.invoke(prompt)
    return jsonify({'result': "success", "chatbot": result.content})
"""
{
  "chatbot": "1. Pixel Forge\n2. GameAlchemy\n3. Quantum Quest\n4. Byte Odyssey\n5. Epic Arcana\n6. LevelUp Labs\n7. DreamGrid Games\n8. NovaPlay Studios\n9. CodeCrafters\n10. Arcane Interactive",
  "result": "success"
}
"""

@app.route('/api/name', methods=['POST'])
def name2():
    data = request.get_json()
    product = data.get("product")
    user_prompt = f"What's a good company name that makes {product}. Do not give any explanation. Just give me the naems."
    print(user_prompt)

    prompt = [
        SystemMessage(content="You are a creative branding expert."),
        HumanMessage(content=user_prompt),
    ]

    result = llm.invoke(prompt)
    return jsonify({'result': "success", "chatbot": result.content})

"""
### 샌드위치 만들기
# C:\src\SPC2026\10.LangChain>curl -X POST localhost:5000/api/name -H "Content-Type: application/json" -d"{"\"product\":\"sandwich\"}
{
  "chatbot": "1. Stack & Layer  \n2. Bread & Bliss  \n3. The Sandwich Spot  \n4. Bite Delight  \n5. Crisp & Crust  \n6. Sub Station  \n7. Slice of Heaven  \n8. Deli Dreams  \n9. Sandwich Symphony  \n10. The Rolling Hoagie",
  "result": "success"
}
"""

@app.route('/api/dinner')
def dinner():

    prompt = [
        SystemMessage(content="당신은 경력 10년차의 호텔 쉐프입니다."),
        HumanMessage(content="오늘의 저녁 메뉴를 추천해줘."),
    ]

    result = llm.invoke(prompt)
    # print(result.content)
    return jsonify({'result': "success", "chatbot": result.content})

"""
{
  "chatbot": "\ubb3c\ub860\uc785\ub2c8\ub2e4! \uc624\ub298\uc758 \uc800\ub141 \uba54\ub274\ub85c\ub294 \ub2e4\uc74c\uacfc \uac19\uc740 \uc870\ud569\uc744 \ucd94\ucc9c\ub4dc\ub9bd\ub2c8\ub2e4.\n\n**\uc560\ud53c\ud0c0\uc774\uc800:**\n- **\uad6c\uc6b4 \uc544\uc2a4\ud30c\ub77c\uac70\uc2a4\uc640 \ud30c\ub974\ub9c8\uc0b0**: \uc544\uc2a4\ud30c\ub77c\uac70\uc2a4\ub97c \uc624\uc77c\uc5d0 \uc0b4\uc9dd \ubcf6\uc544 \uc18c\uae08\uacfc \ud6c4\ucd94\ub85c \uac04\uc744 \ud558\uace0, \ub9c8\uc9c0\ub9c9\uc5d0 \ud30c\ub974\ub9c8\uc0b0 \uce58\uc988\ub97c \uac08\uc544\uc11c \uc62c\ub824\uc90d\ub2c8\ub2e4.\n\n**\uba54\uc778 \uc694\ub9ac:**\n- **\ud5c8\ube0c \ud06c\ub7ec\uc2a4\ud2b8 \uc591\uac08\ube44**: \ub9c8\ub9ac\ub124\uc774\ub4dc \ud55c \uc591\uac08\ube44\ub97c \ud5c8\ube0c\uc640 \ub9c8\ub298\ub85c \ud06c\ub7ec\uc2a4\ud2b8\ub97c \ub9cc\ub4e4\uc5b4 \uad7d\uc2b5\ub2c8\ub2e4. \ud5c8\ube0c\ub294 \ub85c\uc988\ub9c8\ub9ac, \ud0c0\uc784, \uadf8\ub9ac\uace0 \uc624\ub808\uac00\ub178\ub97c \uc11e\uc5b4 \uc0ac\uc6a9\ud558\uc138\uc694.\n- **\uc0ac\uc774\ub4dc \ub514\uc26c: \uac10\uc790 \ud4e8\ub808**: \ubd80\ub4dc\ub7ec\uc6b4 \uac10\uc790 \ud4e8\ub808\ub97c \ub9cc\ub4e4\uc5b4 \uc591\uac08\ube44\uc640 \ud568\uaed8 \uacc1\ub4e4\uc785\ub2c8\ub2e4. \n\n**\ub514\uc800\ud2b8:**\n- **\ucd08\ucf5c\ub9bf \ubb34\uc2a4**: \ub2e4\ud06c \ucd08\ucf5c\ub9bf\uacfc \uc0dd\ud06c\ub9bc\uc744 \uc0ac\uc6a9\ud558\uc5ec \ubd80\ub4dc\ub7fd\uace0 \uc9c4\ud55c \ucd08\ucf5c\ub9bf \ubb34\uc2a4\ub97c \ub9cc\ub4ed\ub2c8\ub2e4. \ub9c8\uc9c0\ub9c9\uc5d0 \ubbfc\ud2b8 \uc78e\uc73c\ub85c \uc7a5\uc2dd\ud574 \uc8fc\uc138\uc694.\n\n**\uc74c\ub8cc:**\n- \ub808\ub4dc \uc640\uc778 \ud55c \uc794, \ud2b9\ud788 \uc591\uac08\ube44\uc640 \uc798 \uc5b4\uc6b8\ub9ac\ub294 \uce98\ub9ac\ud3ec\ub2c8\uc544\uc758 \uce74\ubc84\ub124 \uc18c\ube44\ub1fd\uc744 \ucd94\ucc9c\ud569\ub2c8\ub2e4.\n\n\uc774 \uba54\ub274\ub294 \uace0\uae09\uc2a4\ub7ec\uc6b4 \ub290\ub08c\uc744 \uc8fc\uba74\uc11c\ub3c4 \ub9db\uc788\uace0 \uade0\ud615 \uc7a1\ud78c \uc800\ub141 \uc2dd\uc0ac\ub97c \uc81c\uacf5\ud569\ub2c8\ub2e4. \uc990\uac70\uc6b4 \uc800\ub141 \uc2dd\uc0ac\uac00 \ub418\uae38 \ubc14\ub78d\ub2c8\ub2e4!",
  "result": "success"
}
"""
if __name__ == '__main__':
    app.run(debug=True)

