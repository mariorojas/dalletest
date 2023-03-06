# Test script for DALL-E

**INSTALLATION COMMANDS**

```
git clone https://github.com/mariorojas/dalletest.git
cd dalletest/
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Make sure to get your [OpenAI API key](https://platform.openai.com/account/api-keys) and set it in **main.py**

```
openai.api_key = 'your-key'
```

To create an image, run the following:

```
python main.py
# output: https://...
```

To create more than 1 image, increase `n` values in **main.py**.

Please consider this value can increase credit cost.

```
response = openai.Image.create(
    ...
    n=1
)
```
