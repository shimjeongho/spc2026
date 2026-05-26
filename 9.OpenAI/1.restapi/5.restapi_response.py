import os
import requests
from dotenv import load_dotenv

load_dotenv() # 내가 읽어갈 경로르 지정할수도 있음

openai_api_key = os.getenv('OPENAI_API_KEY')

user_input = "대한민국의 수도는 어디야?"

response =requests.post (
    'https://api.openai.com/v1/responses',
     headers = {
         "Content-Type": 'application/json',
         'Authorization' : f'Bearer {openai_api_key}'
     },
     json={
         
         'model': 'gpt-4o-mini',
         'input':user_input,
     }
)

data =response.json()
print(data)
print('-' *30)
answer = data['output'][0]['content'][0]['text']
print('응답: ', answer)

"""
{'id': 'resp_09db48a875557204006a14f54d3dec819993f8601a7819df38', 'object': 'response', 'created_at': 1779758413, 'status': 'completed', 'background': False, 'billing': {'payer': 'openai'}, 'completed_at': 1779758413, 'error': None, 'frequency_penalty': 0.0, 'incomplete_details': None, 'instructions': None, 'max_output_tokens': None, 'max_tool_calls': None, 'model': 'gpt-4o-mini-2024-07-18', 'moderation': None, 'output': [{'id': 'msg_09db48a875557204006a14f54dbf94819997ad23742abed515', 'type': 'message', 'status': 'completed', 'content': [{'type': 'output_text', 'annotations': [], 'logprobs': [], 'text': '대한민국의 수도는 서울입니다.'}], 'role': 'assistant'}], 'parallel_tool_calls': True, 'presence_penalty': 0.0, 'previous_response_id': None, 'prompt_cache_key': None, 'prompt_cache_retention': 'in_memory', 'reasoning': {'context': None, 'effort': None, 'summary': None}, 'safety_identifier': None, 'service_tier': 'default', 'store': True, 'temperature': 1.0, 'text': {'format': {'type': 'text'}, 'verbosity': 'medium'}, 'tool_choice': 'auto', 'tools': [], 'top_logprobs': 0, 'top_p': 1.0, 'truncation': 'disabled', 'usage': {'input_tokens': 15, 'input_tokens_details': {'cached_tokens': 0}, 'output_tokens': 9, 'output_tokens_details': {'reasoning_tokens': 0}, 'total_tokens': 24}, 'user': None, 'metadata': {}}
------------------------------
응답:  대한민국의 수도는 서울입니다.
"""