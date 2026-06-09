from mcp.server.fastmcp import FastMCP
from datetime import datetime

# mcp = FastMCP("my-http-mcp-server",port=5555)
mcp = FastMCP("my-http-mcp-server")  # 기본값은 8000 임

@mcp.tool()
def hello(name: str) -> str:
    """ 사용자에게 인사말을 생성하는 도구 

        매개변수:
            name (str): 인사말 대상의 이름

        반환값:
            str: "Hello, {name}!" 형태의 인사말
    """

    return f"Hello, {name}!"

@mcp.tool()
def add(a: int, b: int) -> int:
    """ 두 정수의 덧셈을 수행하는 계산 도구 """
    return a + b

@mcp.tool()
def now() -> str:
    """ 현재 시간을 한국어로 포멧하여 반환하는 도구 """
    return datetime.now().strftime("지금 시간은 %Y-%m-%d %H:%M:%S 입니다.")

if __name__ == "__main__":
    mcp.run(transport="streamable-http")    # < - 이거 한줄 한단어로 stdio -> http 서버로 전환


"""
INFO:     Started server process [5456]
INFO:     Waiting for application startup.
[06/09/26 12:16:46] INFO     StreamableHTTP session manager started                                                                                                         streamable_http_manager.py:131
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

(py312) C:\src\SPC2026\12.ANTHROPIC\3.mcp>python 9.mcp_http_client.py
도구:  ['hello', 'add', 'now']


[06/09/26 12:17:22] INFO     Created new transport with session ID: c966632ef5264fff8b55d768271fc2ab                                                                        streamable_http_manager.py:281
INFO:     127.0.0.1:65170 - "POST /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:65173 - "GET /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:65174 - "POST /mcp HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:65176 - "POST /mcp HTTP/1.1" 200 OK
[06/09/26 12:17:23] INFO     Processing request of type ListToolsRequest                                                                                                                     server.py:727
                    INFO     Terminating session: c966632ef5264fff8b55d768271fc2ab                                                                                                  streamable_http.py:785
INFO:     127.0.0.1:65178 - "DELETE /mcp HTTP/1.1" 200 OK
"""
