from openai import OpenAI
def openai_chat_completion(cred,params):
    try:
        if "prompt" in params and 'apiKey' in cred:
            if 'org' in cred:
                openai_client = OpenAI(api_key=cred['apiKey'], organization=cred["org"])
            else:
                openai_client = OpenAI(api_key=cred['apiKey'])
            if 'optional' in params:
                data={}
                for key, value in params["optional"].items():
                    if value:
                        data[key] = value
                completion = openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content":params["prompt"]}
                ],
                **data
            )
            else:
                completion = openai_client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content":params["prompt"]}
                    ]
                )
            if params["simplify"]:
                return completion.choices[0].message.content
            else:
                completion_dict={
                "id": completion.id,
                "choices": [
                    {
                        "finish_reason": choice.finish_reason,
                        "index": choice.index,
                        "logprobs": choice.logprobs,
                        "message_content": choice.message.content if choice.message else None
                    }
                    for choice in completion.choices
                ],
                "created":completion.created,
                "model":completion.model,
                "object":completion.object,
                "system_fingerprint":completion.system_fingerprint,
                "usage": {
                    "completion_tokens":completion.usage.completion_tokens,
                    "prompt_tokens":completion.usage.prompt_tokens,
                    "total_tokens":completion.usage.total_tokens
                }
            }
                return completion_dict
        else:
            raise Exception('Missing parameters')
    except Exception as e:
        raise Exception(e)
