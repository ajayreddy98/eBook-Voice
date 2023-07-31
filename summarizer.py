import openai

def summarizeIt(prompt,key, model="gpt-3.5-turbo"):
    openai.api_key = key
    prompt = f"""You are the ebook or book summary bot.
    Please provide the summary for the given text data in atleast 500-600 words in three-four paragraphs.
    PROMPT:{prompt}
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
   )
    return response.choices[0].message["content"]
