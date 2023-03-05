import openai

openai.api_key = 'your-key'
response = openai.Image.create(
    prompt="A photo of a white fur monster standing in a purple room",
    size="1024x1024",
    n=1
)

for el in response.data:
    print(el.url)
