import boto3
import json

prompt_data = """
Act as Shakespeare and compose a poem on Generative AI.
Write exactly 4 lines, no more and no less.
Each line must be written in Shakespearean style.
"""


# Bedrock runtime client
bedrock = boto3.client(service_name="bedrock-runtime")

# OpenAI-compatible schema
payload = {
    "model": "openai.gpt-oss-20b-1:0",
    "messages": [
        {"role": "user", "content": prompt_data}
    ],
    "max_completion_tokens": 512,
    "temperature": 0.5,
    "top_p": 0.9
}

body = json.dumps(payload)

# Invoke the model
response = bedrock.invoke_model(
    body=body,
    modelId="openai.gpt-oss-20b-1:0",
    accept="application/json",
    contentType="application/json"
)

# Parse the response
response_body = json.loads(response["body"].read())
response_text = response_body["choices"][0]["message"]["content"]

print(response_text)

