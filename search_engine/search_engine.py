def search(docs: list[dict[str, str]], word: str) -> list[str]:
    result = []
    for doc in docs:
        if word not in doc["text"]:
            continue

        result.append(doc["id"])
    return result
