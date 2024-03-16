import openai, json
from pprint import pprint

def call_qwen(query, functions=None):
    print('input:')
    messages = [{"role":"system","content":"You are an useful AI assistant that helps people solve the problem step by step."}]
    message_prompt = {"role":"user","content":query}
    messages.append(message_prompt)
    pprint(messages, indent=2)
    openai.api_base = 'http://localhost:8009/v1'
    openai.api_key = 'none'
    if functions:
        response = openai.ChatCompletion.create(model='Qwen',
                                                messages=messages,
                                                functions=functions)
    else:
        response = openai.ChatCompletion.create(model='Qwen',
                                                messages=messages)
    # while response.finish_reason == "function_call":
    response = json.loads(json.dumps(response,
                                     ensure_ascii=False))
    print(f"******************之前的response{response}")
    # response = response.choices[0]['message']
    # response = json.loads(json.dumps(response,
    #                                  ensure_ascii=False))  # fix zh rendering
    print('output:')
    print(response)
    pprint(response, indent=2)
    return response
def test():
    functions = [
            {
                'name_for_human':
                '谷歌搜索',
                'name_for_model':
                'google_search',
                'description_for_model':
                '谷歌搜索是一个通用搜索引擎，可用于访问互联网、查询百科知识、了解时事新闻等。' +
                ' Format the arguments as a JSON object.',
                'parameters': [{
                    'name': 'search_query',
                    'description': '搜索关键词或短语',
                    'required': True,
                    'schema': {
                        'type': 'string'
                    },
                }],
            },
            {
                'name_for_human':
                '文生图',
                'name_for_model':
                'image_gen',
                'description_for_model':
                '文生图是一个AI绘画（图像生成）服务，输入文本描述，返回根据文本作画得到的图片的URL。' +
                ' Format the arguments as a JSON object.',
                'parameters': [{
                    'name': 'prompt',
                    'description': '英文关键词，描述了希望图像具有什么内容',
                    'required': True,
                    'schema': {
                        'type': 'string'
                    },
                }],
            },
        ]
    call_qwen('搜索一下谁是周杰伦',functions)
test()

