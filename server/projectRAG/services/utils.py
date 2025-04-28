def custom_chunk(text):
    import re

    pattern = r'([A-Z][a-z]+(?:\s[A-Z][a-z]+){0,2}\s(?:is made with|is made from).*?kcal\.)'
    chunks = re.split(pattern, text)

    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
    return chunks
