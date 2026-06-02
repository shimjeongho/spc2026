from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent 
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import AIMessage

load_dotenv()

checkpoint = MemorySaver()

@tool
def send_payment(recipient: str, amount: int) -> str:
    """ 수신자에게 지정 금액을 송금한다."""
    return f"{recipient} 에게 {amount} 원 송금 완료"

@tool
def get_balance(account: str) -> int:
    """ 계좌 잔액 조회 """
    return {"alice": 1_000_000, "bob": 500_000}.get(account, 0)

llm = ChatOpenAI(model="gpt-4o-mini")
agent = create_agent(llm, [send_payment, get_balance], checkpointer=checkpoint, interrupt_before=["tools"])

config = {"configurable": {"thread_id": "t001"}}

question = "bob에게 1만원을 송금해."

print(f"[유저] {question}")
result = agent.invoke({"messages": [("user", question)]}, config=config)
print('=' * 30)
print(result)
print('=' * 30)

# 1. 현재 멈춰 있는 상태 조회
ai_msg = agent.get_state(config).values["messages"][-1]
call = ai_msg.tool_calls[0]
args = call['args']

print(f"[에이전트 제안] {call['name']} ({call['args']})")


# 2. 해당 상태를 어떻게 처리할건지, 사용자에게 물어보기
print(f"\n{args['recipient']} 에게 송금을 진행하시겠습니까?")
print("  1. 예(송금)")
print("  2. 아니오(취소)")
print("  3. 금액 수정")
choice = input("선택 (1/2/3): ").strip()

if choice == "2":
    print("\n[취소] 사용자 요청에 의해 취소되었습니다.")
else:
    if choice == "3":
        new_amount = int(input("새 송금 금액(원) 을 입력하세요: ").strip())
        edited = {**call, "args": {**call['args'], 'amount': new_amount}}

        fixed = AIMessage(content=ai_msg.content, tool_calls=[edited], id=ai_msg.id)
        agent.update_state(config, {"messages": [fixed]})
        print(f"사람이 수정했음 10000 -> {new_amount}")

    # 3. 다시 이어서 실행한다.
    result = agent.invoke(None, config=config)  # 할일을 계속 이어서 하시오
    final = result["messages"][-1].content
    if not final:
        final = result["messages"][-2].content
    print(f"[최종] {final}")


# 1
"""
[유저] bob에게 1만원을 송금해.
==============================
{'messages': [HumanMessage(content='bob에게 1만원을 송금해.', additional_kwargs={}, response_metadata={}, id='7ae4ff37-af86-4cb1-9a68-83a9dcce8d4f'), AIMessage(content='', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 19, 'prompt_tokens': 83, 'total_tokens': 102, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_d682aea597', 'id': 'chatcmpl-DmCX6j3t3qj758MATVlVr5SyNCEUb', 'service_tier': 'default', 'finish_reason': 'tool_calls', 'logprobs': None}, id='lc_run--019e86ef-53f4-7343-aa81-3c60d1c48929-0', tool_calls=[{'name': 'send_payment', 'args': {'recipient': 'bob', 'amount': 10000}, 'id': 'call_n8o9LmIdxKw5tyKqVpbCTJhx', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 83, 'output_tokens': 19, 'total_tokens': 102, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}
==============================
[에이전트 제안] send_payment ({'recipient': 'bob', 'amount': 10000})

bob 에게 송금을 진행하시겠습니까?
  1. 예(송금)
  2. 아니오(취소)
  3. 금액 수정s
선택 (1/2/3): 1
[최종] bob에게 1만원이 송금되었습니다.
"""


# 2
"""
[유저] bob에게 1만원을 송금해.
==============================
{'messages': [HumanMessage(content='bob에게 1만원을 송금해.', additional_kwargs={}, response_metadata={}, id='95d34f97-ac90-40ee-b641-6313d8151f5f'), AIMessage(content='', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 19, 'prompt_tokens': 83, 'total_tokens': 102, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_d682aea597', 'id': 'chatcmpl-DmCXN6GzCXtyQ25esF5yscdaco3rY', 'service_tier': 'default', 'finish_reason': 'tool_calls', 'logprobs': None}, id='lc_run--019e86ef-983a-7293-9ac9-9af7b6c99669-0', tool_calls=[{'name': 'send_payment', 'args': {'recipient': 'bob', 'amount': 10000}, 'id': 'call_985BwLtSK1tliu2EXSH05o2g', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 83, 'output_tokens': 19, 'total_tokens': 102, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}
==============================
[에이전트 제안] send_payment ({'recipient': 'bob', 'amount': 10000})

bob 에게 송금을 진행하시겠습니까?
  1. 예(송금)
  2. 아니오(취소)
  3. 금액 수정
선택 (1/2/3): 2

[취소] 사용자 요청에 의해 취소되었습니다.
"""

# 3
"""

[유저] bob에게 1만원을 송금해.
==============================
{'messages': [HumanMessage(content='bob에게 1만원을 송금해.', additional_kwargs={}, response_metadata={}, id='93ca5e7d-83b7-4d0e-ace0-771e4ac729ca'), AIMessage(content='', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 19, 'prompt_tokens': 84, 'total_tokens': 103, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_53ee395669', 'id': 'chatcmpl-DmCZ4jMoKM2PyiXnkY37wrQn8AHRZ', 'service_tier': 'default', 'finish_reason': 'tool_calls', 'logprobs': None}, id='lc_run--019e86f1-31f0-74c2-9fe2-c0b2d366035a-0', tool_calls=[{'name': 'send_payment', 'args': {'recipient': 'bob', 'amount': 10000}, 'id': 'call_bvd7TkT3aED5e9994qCkxmD2', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 84, 'output_tokens': 19, 'total_tokens': 103, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}
==============================
[에이전트 제안] send_payment ({'recipient': 'bob', 'amount': 10000})

bob 에게 송금을 진행하시겠습니까?
  1. 예(송금)
  2. 아니오(취소)
  3. 금액 수정
선택 (1/2/3): 3
새 송금 금액(원) 을 입력하세요: 5000
사람이 수정했음 10000 -> 5000
[최종] bob 에게 5000 원 송금 완료

"""