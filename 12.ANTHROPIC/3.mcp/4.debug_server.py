# fastapi <-- flask 떠올리면 됨

import sys
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("HelloWorld")

@mcp.tool()
def hello(name: str) -> str:
    print(f"[SERVER] hello 함수 호출됨: name={name}", file=sys.stderr) # 통신에 관여하지 않기 위해 stdrr로 출력 (그냥은 stdout 출력하고 있음)
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(f"[SERVER] 서버가 시작됨", file=sys.stderr)
    mcp.run()