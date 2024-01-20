from openai import OpenAI

client = OpenAI()

summary_configuration = dict(
    model="gpt-4-1106-preview",
    temperature=0.1,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)


def _summarise(content_type: str, code: str, max_tokens: int) -> str:
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant who helps to summarise code."
            },
            {
                "role": "user",
                "content": f"What is the purpose of this {content_type}, one liner?\n\n{code}"
            }
        ],
        max_tokens=max_tokens,
        **summary_configuration,
    )

    return response.choices[0].message.content

def summarise_code(code: str, max_tokens: int = 100) -> str:
    return _summarise("function", code, max_tokens)


def summarise_class(code: str, max_tokens: int = 100) -> str:
    return _summarise("class", code, max_tokens)

def summarise_code(code: str, max_tokens: int = 100) -> str:
    return _summarise("function", code, max_tokens)


def summarise_file(code: str, max_tokens: int = 100) -> str:
    return _summarise("module/file", code, max_tokens)
