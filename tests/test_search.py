from search_engine.search_engine import search


def test_search_empty_collection():
    assert search([], "something") == []


def test_search_find_exists():
    assert search(
        [
            {"id": "doc1", "text": "I am new hexlet boy"},
            {"id": "doc2", "text": "Is hexlet a programmers site?"},
            {"id": "doc3", "text": "small cow says moooooo"},
        ],
        "hex",
    ) == ["doc1", "doc2"]


def test_search_no_match():
    assert (
        search(
            [
                {"id": "doc1", "text": "I am new hexlet boy"},
                {"id": "doc2", "text": "Is hexlet a programmers site?"},
                {"id": "doc3", "text": "small cow says moooooo"},
            ],
            "Duck",
        )
        == []
    )
