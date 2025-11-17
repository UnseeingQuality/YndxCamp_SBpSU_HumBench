import os

YANDEX_CLOUD_FOLDER = os.getenv('YANDEX_CLOUD_FOLDER')
YANDEX_CLOUD_API_KEY = os.getenv('YANDEX_CLOUD_API_KEY')
YANDEX_CLOUD_MODEL = os.getenv('YANDEX_CLOUD_MODEL')
VECTOR_STORE_IDS = []

client = openai.OpenAI(
    api_key=YANDEX_CLOUD_API_KEY,
    base_url="https://rest-assistant.api.cloud.yandex.net/v1",
    project=YANDEX_CLOUD_FOLDER
)

response = client.responses.create(
    model=f"gpt://{YANDEX_CLOUD_FOLDER}/{YANDEX_CLOUD_MODEL}",
    temperature=0.3,
    instructions="",
    tools=[{
        "file_search": {
            "vector_store_ids": VECTOR_STORE_IDS
        }
    }],
    input="Суммаризируй текст, который я напишу в следующем сообщении. Задача понятна?",
    #max_output_tokens=500
)

print(response.output_text)