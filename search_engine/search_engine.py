import re


def delete_punctuation(word: str) -> str:
    return "".join(re.findall(r"\w+", word)).lower()


def search(docs: list[dict[str, str]], word: str) -> list[str]:
    result = []
    rank = []
    term = delete_punctuation(word)
    for doc in docs:
        words = list(map(delete_punctuation, doc["text"].split()))
        match_count = len(list(filter(lambda x: x == term, words)))
        if match_count == 0:
            continue

        result.append(doc["id"])
        rank.append(match_count)
        i = len(rank) - 2
        while i >= 0 and rank[i] < match_count:
            rank[i], rank[i + 1] = rank[i + 1], rank[i]
            result[i], result[i + 1] = result[i + 1], result[i]
    return result
