import re


def search(docs: list[dict[str, str]], word: str) -> list[str]:
    result = []
    term = "".join(re.findall(r"\w+", word)).lower()
    for doc in docs:
        if term not in doc["text"]:
            continue

        result.append(doc["id"])
    return result
