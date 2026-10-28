import os

from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),
)
message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "content": "Hello, how are you?",
            "role": "user",
        }
    ],
    model="claude-haiku-5-5",
)
print(message.content[0].text)

