from openai import OpenAI

client = OpenAI()

summary_configuration = dict(
    model="gpt-4-1106-preview",
    temperature=0.1,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)


def summarise_code(code: str, max_tokens: int = 100) -> str:
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant who helps to summarise code."
            },
            {
                "role": "user",
                "content": f"What is the purpose of this function, one liner?\n\n{code}"
            }
        ],
        max_tokens=max_tokens,
        **summary_configuration,
    )

    return response.choices[0].message.content
