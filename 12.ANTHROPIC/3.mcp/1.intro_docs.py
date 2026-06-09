# pip install mcp
import mcp
from mcp.server.fastmcp import FastMCP
from mcp import ClientSession

from importlib.metadata import version
import inspect

print(f"MCP version: {version('mcp')}") # MCP version: 1.27.2

print("\nMCP 문서\n-------------")
print(inspect.getdoc(FastMCP))

"""
MCP 문서
-------------
Abstract base class for generic types.

On Python 3.12 and newer, generic classes implicitly inherit from
Generic when they declare a parameter list after the class's name::

    class Mapping[KT, VT]:
        def __getitem__(self, key: KT) -> VT:
            ...
        # Etc.

On older versions of Python, however, generic classes have to
explicitly inherit from Generic.

After a class has been declared to be generic, it can then be used as
follows::

    def lookup_name[KT, VT](mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
        try:
            return mapping[key]
        except KeyError:
            return default
a
"""

print(inspect.getdoc(FastMCP.sse_app))

print("\nMCP 세션 관리 문서\n------")
print(inspect.getdoc(ClientSession))
print(inspect.getdoc(ClientSession.initialize))
"""
MCP 세션 관리 문서
------
Implements an MCP "session" on top of read/write streams, including features
like request/response linking, notifications, and progress.

This class is an async context manager that automatically starts processing
messages when entered.
None
"""