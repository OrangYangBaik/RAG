import re

def custom_chunk(text):
    pattern = r'([A-Z][a-z]+(?:\s[A-Z][a-z]+){0,2}\s(?:is made with|is made from).*?kcal\.)'
    matches = re.findall(pattern, text)

    return [match.strip() for match in matches]