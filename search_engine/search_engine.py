import re


def delete_punctuation(word: str) -> str:
    return "".join(re.findall(r"\w+", word)).lower()


def get_match_stat(terms: list[str], words: list[str]) -> tuple[int, int]:
    matched_set = set()
    matched_words_num, all_matches_num = 0, 0
    for word in words:
        if word not in terms:
            continue

        all_matches_num += 1

        if word not in matched_set:
            matched_words_num += 1
            matched_set.add(word)
    return matched_words_num, all_matches_num


def search(docs: list[dict[str, str]], sentence: str) -> list[str]:
    result = []
    rank = []
    terms = list(map(delete_punctuation, sentence.split()))
    for doc in docs:
        words = list(map(delete_punctuation, doc["text"].split()))
        matched_words_num, all_matches_num = get_match_stat(terms, words)
        if matched_words_num == 0:
            continue

        result.append(doc["id"])
        rank.append((matched_words_num, all_matches_num))
        i = len(rank) - 2
        while i >= 0 and (
            rank[i][0] < matched_words_num
            or (rank[i][0] == matched_words_num and rank[i][1] < all_matches_num)
        ):
            rank[i], rank[i + 1] = rank[i + 1], rank[i]
            result[i], result[i + 1] = result[i + 1], result[i]
    return result
