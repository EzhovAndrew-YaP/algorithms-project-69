import math
import re


def delete_punctuation(word: str) -> str:
    return "".join(re.findall(r"\w+", word)).lower()


def build_index(
    docs: list[dict[str, str]]
) -> tuple[dict[str, dict[str, int]], dict[str, int]]:
    index: dict[str, dict[str, int]] = {}
    words_docs_num: dict[str, int] = {}
    for doc in docs:
        words = list(map(delete_punctuation, doc["text"].split()))
        words_docs_num[doc["id"]] = len(words)
        for word in words:
            if word not in index:
                index[word] = {doc["id"]: 1}
                continue
            if doc["id"] not in index[word]:
                index[word][doc["id"]] = 1
                continue
            index[word][doc["id"]] += 1
    return index, words_docs_num


def tf_idf(
    word_doc_number: int,
    doc_all_words_number: int,
    docs_number: int,
    docs_with_word: int,
) -> int:
    tf = word_doc_number / doc_all_words_number
    idf = math.log2(1 + (docs_number - docs_with_word + 1) / (docs_with_word + 0.5))
    return tf * idf


def search(docs: list[dict[str, str]], sentence: str) -> list[str]:
    if not sentence:
        return docs
    result = []
    rank = []
    docs_number = len(docs)
    terms = list(map(delete_punctuation, sentence.split()))
    revert_index, words_docs_num = build_index(docs=docs)
    docs_candidates_ids = set()
    for term in terms:
        term_doc_ids = revert_index.get(term, {})
        docs_candidates_ids |= term_doc_ids.keys()
    for doc_id in docs_candidates_ids:
        doc_tf_idf = 0
        for term in terms:
            if doc_id not in revert_index[term]:
                continue
            doc_tf_idf += tf_idf(
                word_doc_number=revert_index[term][doc_id],
                doc_all_words_number=words_docs_num[doc_id],
                docs_number=docs_number,
                docs_with_word=len(revert_index[term].keys()),
            )

        result.append(doc_id)
        rank.append(doc_tf_idf)
        i = len(rank) - 2
        while i >= 0 and rank[i] < doc_tf_idf:
            rank[i], rank[i + 1] = rank[i + 1], rank[i]
            result[i], result[i + 1] = result[i + 1], result[i]
            i -= 1
    return result
