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
print('응답ID: ', data['id'])

response_id = data['id']

user_input = "그 도시의 인구는 몇이야?"

response =requests.post (
    'https://api.openai.com/v1/responses',
     headers = {
         "Content-Type": 'application/json',
         'Authorization' : f'Bearer {openai_api_key}'
     },
     json={
         
         'model': 'gpt-4o-mini',
         'input':user_input,
         'previous_response_id': response_id
     }
)

data =response.json()
print(data)
print('-' *30)
answer = data['output'][0]['content'][0]['text']
print('응답: ', answer)
print('응답ID: ', data['id'])

user_input = "그 도시에서 가볼만한 곳 세곳만 추천해줘"

response =requests.post (
    'https://api.openai.com/v1/responses',
     headers = {
         "Content-Type": 'application/json',
         'Authorization' : f'Bearer {openai_api_key}'
     },
     json={
         
         'model': 'gpt-4o-mini',
         'input':user_input,
         'previous_response_id': response_id
     }
)

data =response.json()
print(data)
print('-' *30)
answer = data['output'][0]['content'][0]['text']
print('응답: ', answer)
print('응답ID: ', data['id'])

"""
{'id': 'resp_05814c6824d9e023006a14f670fe5081998f9272574bc7f0e2', 'object': 'response', 'created_at': 1779758705, 'status': 'completed', 'background': False, 'billing': {'payer': 'openai'}, 'completed_at': 1779758705, 'error': None, 'frequency_penalty': 0.0, 'incomplete_details': None, 'instructions': None, 'max_output_tokens': None, 'max_tool_calls': None, 'model': 'gpt-4o-mini-2024-07-18', 'moderation': None, 'output': [{'id': 'msg_05814c6824d9e023006a14f67199d8819982f73000cd0857ef', 'type': 'message', 'status': 'completed', 'content': [{'type': 'output_text', 'annotations': [], 'logprobs': [], 'text': '대한민국의 수도는 서울입니다.'}], 'role': 'assistant'}], 'parallel_tool_calls': True, 'presence_penalty': 0.0, 'previous_response_id': None, 'prompt_cache_key': None, 'prompt_cache_retention': 'in_memory', 'reasoning': {'context': None, 'effort': None, 'summary': None}, 'safety_identifier': None, 'service_tier': 'default', 'store': True, 'temperature': 1.0, 'text': {'format': {'type': 'text'}, 'verbosity': 'medium'}, 'tool_choice': 'auto', 'tools': [], 'top_logprobs': 0, 'top_p': 1.0, 'truncation': 'disabled', 'usage': {'input_tokens': 15, 'input_tokens_details': {'cached_tokens': 0}, 'output_tokens': 9, 'output_tokens_details': {'reasoning_tokens': 0}, 'total_tokens': 24}, 'user': None, 'metadata': {}}
------------------------------
응답:  대한민국의 수도는 서울입니다.
응답ID:  resp_05814c6824d9e023006a14f670fe5081998f9272574bc7f0e2
{'id': 'resp_05814c6824d9e023006a14f6722da881998f282e1dafb23c18', 'object': 'response', 'created_at': 1779758706, 'status': 'completed', 'background': False, 'billing': {'payer': 'openai'}, 'completed_at': 1779758707, 'error': None, 'frequency_penalty': 0.0, 'incomplete_details': None, 'instructions': None, 'max_output_tokens': None, 'max_tool_calls': None, 'model': 'gpt-4o-mini-2024-07-18', 'moderation': None, 'output': [{'id': 'msg_05814c6824d9e023006a14f672d2a88199b3ba831c8af91711', 'type': 'message', 'status': 'completed', 'content': [{'type': 'output_text', 'annotations': [], 'logprobs': [], 'text': '서울의 인구는 약 9백만 명 정도입니다. 하지만 인구는 지속적으로 변할 수 있으니, 최신 통계를 확인하는 것이 좋습니다.'}], 'role': 'assistant'}], 'parallel_tool_calls': True, 'presence_penalty': 0.0, 'previous_response_id': 'resp_05814c6824d9e023006a14f670fe5081998f9272574bc7f0e2', 'prompt_cache_key': None, 'prompt_cache_retention': 'in_memory', 'reasoning': {'context': None, 'effort': None, 'summary': None}, 'safety_identifier': None, 'service_tier': 'default', 'store': True, 'temperature': 1.0, 'text': {'format': {'type': 'text'}, 'verbosity': 'medium'}, 'tool_choice': 'auto', 'tools': [], 'top_logprobs': 0, 'top_p': 1.0, 'truncation': 'disabled', 'usage': {'input_tokens': 41, 'input_tokens_details': {'cached_tokens': 0}, 'output_tokens': 36, 'output_tokens_details': {'reasoning_tokens': 0}, 'total_tokens': 77}, 'user': None, 'metadata': {}}
------------------------------
응답:  서울의 인구는 약 9백만 명 정도입니다. 하지만 인구는 지속적으로 변할 수 있으니, 최신 통계를 확인하는 것이 좋습니다.
응답ID:  resp_05814c6824d9e023006a14f6722da881998f282e1dafb23c18
{'id': 'resp_05814c6824d9e023006a14f6739b608199a126839b6e6b7b63', 'object': 'response', 'created_at': 1779758707, 'status': 'completed', 'background': False, 'billing': {'payer': 'openai'}, 'completed_at': 1779758709, 'error': None, 'frequency_penalty': 0.0, 'incomplete_details': None, 'instructions': None, 'max_output_tokens': None, 'max_tool_calls': None, 'model': 'gpt-4o-mini-2024-07-18', 'moderation': None, 'output': [{'id': 'msg_05814c6824d9e023006a14f67403fc81998283114367255618', 'type': 'message', 'status': 'completed', 'content': [{'type': 'output_text', 'annotations': [], 'logprobs': [], 'text': '서울에서 가볼 만한 곳 세 곳을 추천해 드릴게요:\n\n1. **경복궁**: 대한민국의 대표적인 궁궐로, 조선 시대의 역사와 문화를 체험할 수 있는 곳입니다. 전통 건축과 아름다운 정원이 매력적입니다.\n\n2. **북촌 한옥마을**: 전통 한옥이 잘 보존되어 있는 지역으로, 고즈넉한 분위기 속에서 한국의 전통 문화를 느낄 수 있습니다. 이곳에서는 사진 찍기에도 좋은 장소가 많습니다.\n\n3. **명동**: 쇼핑과 먹거리가 가득한 서울의 중심 상업지구입니다. 다양한 음식과 패션 아이템을 즐길 수 있으며, 거리 공연도 종종 열립니다.\n\n이 외에도 서울에는 다양한 볼거리와 즐길거리가 많으니 꼭 방문해 보세요!'}], 'role': 'assistant'}], 'parallel_tool_calls': True, 'presence_penalty': 0.0, 'previous_response_id': 'resp_05814c6824d9e023006a14f670fe5081998f9272574bc7f0e2', 'prompt_cache_key': None, 'prompt_cache_retention': 'in_memory', 'reasoning': {'context': None, 'effort': None, 'summary': None}, 'safety_identifier': None, 'service_tier': 'default', 'store': True, 'temperature': 1.0, 'text': {'format': {'type': 'text'}, 'verbosity': 'medium'}, 'tool_choice': 'auto', 'tools': [], 'top_logprobs': 0, 'top_p': 1.0, 'truncation': 'disabled', 'usage': {'input_tokens': 45, 'input_tokens_details': {'cached_tokens': 0}, 'output_tokens': 192, 'output_tokens_details': {'reasoning_tokens': 0}, 'total_tokens': 237}, 'user': None, 'metadata': {}}
------------------------------
응답:  서울에서 가볼 만한 곳 세 곳을 추천해 드릴게요:

1. **경복궁**: 대한민국의 대표적인 궁궐로, 조선 시대의 역사와 문화를 체험할 수 있는 곳입니다. 전통 건축과 아름다운 정원이 매력적입니다.

2. **북촌 한옥마을**: 전통 한옥이 잘 보존되어 있는 지역으로, 고즈넉한 분위기 속에서 한국의 전통 문화를 느낄 수 있습니다. 이곳에서는 사진 찍기에도 좋은 장소가 많습니다.

3. **명동**: 쇼핑과 먹거리가 가득한 서울의 중심 상업지구입니다. 다양한 음식과 패션 아이템을 즐길 수 있으며, 거리 공연도 종종 열립니다.

이 외에도 서울에는 다양한 볼거리와 즐길거리가 많으니 꼭 방문해 보세요!
응답ID:  resp_05814c6824d9e023006a14f6739b608199a126839b6e6b7b63
"""