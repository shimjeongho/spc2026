from langchain_community.agent_toolkits.load_tools import get_all_tool_names

print('--- load_tools를 통해서 가져올수 있는 모든 도구 ---')
names = sorted(get_all_tool_names())

for name in names:
    print(f" - {name}")


print(f"\n총 {len(names)} 개 가 현재 사용 가능")

"""
--- load_tools를 통해서 가져올수 있는 모든 도구 ---
 - arxiv
 - awslambda
 - bing-search
 - dalle-image-generator
 - dataforseo-api-search
 - dataforseo-api-search-json
 - ddg-search
 - eleven_labs_text2speech
 - golden-query
 - google-books
 - google-finance
 - google-jobs
 - google-lens
 - google-scholar
 - google-serper
 - google-serper-results-json
 - google-trends
 - google_cloud_texttospeech
 - graphql
 - human
 - llm-math
 - memorize
 - merriam-webster
 - metaphor-search
 - news-api
 - open-meteo-api
 - openweathermap-api
 - podcast-api
 - pubmed
 - read_file
 - reddit_search
 - requests
 - requests_delete
 - requests_get
 - requests_patch
 - requests_post
 - requests_put
 - sceneXplain
 - searchapi
 - searchapi-results-json
 - searx-search
 - searx-search-results-json
 - serpapi
 - sleep
 - stackexchange
 - terminal
 - tmdb-api
 - twilio
 - wikipedia
 - wolfram-alpha

총 50 개 가 현재 사용 가능
"""

