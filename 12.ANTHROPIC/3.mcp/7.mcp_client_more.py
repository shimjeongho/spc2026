import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params = StdioServerParameters(command="python", args=["6.mcp_server_moretools.py"])

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 너 어떤 도구니?
            tools = (await session.list_tools()).tools
            print("도구: ", tools)

            result = (await session.call_tool("add", {"a": 3, "b": 5})).content[0].text
            print("add도구 호출결과: ", result)

            result = (await session.call_tool("word_count", {"text":"너는 어떤 서버니?"})).content[0].text
            print("word_count 도구 호출결과: ", result)

if __name__ == "__main__":
    asyncio.run(main())

"""
도구:  [Tool(name='add', title=None, description=' 두 정수 a와 b를 더한다.', inputSchema={'properties': {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}, 'required': ['a', 'b'], 'title': 'addArguments', 'type': 'object'}, outputSchema={'properties': {'result': {'title': 'Result', 'type': 'integer'}}, 'required': ['result'], 'title': 'addOutput', 'type': 'object'}, icons=None, annotations=None, meta=None, execution=None), Tool(name='multiply', title=None, description=' 두 정수 a와 b를 곱한다.', inputSchema={'properties': {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}, 'required': ['a', 'b'], 'title': 'multiplyArguments', 'type': 'object'}, outputSchema={'properties': {'result': {'title': 'Result', 'type': 'integer'}}, 'required': ['result'], 'title': 'multiplyOutput', 'type': 'object'}, icons=None, annotations=None, meta=None, execution=None), Tool(name='word_count', title=None, description=' 주어진 문장에서 단어 갯수를 센다 ', inputSchema={'properties': {'text': {'title': 'Text', 'type': 'string'}}, 'required': ['text'], 'title': 'word_countArguments', 'type': 'object'}, outputSchema={'properties': {'result': {'title': 'Result', 'type': 'integer'}}, 'required': ['result'], 'title': 'word_countOutput', 'type': 'object'}, icons=None, annotations=None, meta=None, execution=None)]
add도구 호출결과:  8
word_count 도구 호출결과:  3
"""