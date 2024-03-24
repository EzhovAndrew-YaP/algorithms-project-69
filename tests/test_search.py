from search_engine.search_engine import search


def test_search_empty_collection():
    assert search([], "something") == []


def test_search_no_sentence():
    assert search(
        [{"id": "doc1", "text": "I am new hex let boy, dude"}], ""
    ) == [{"id": "doc1", "text": "I am new hex let boy, dude"}]


def test_search_find_exists():
    assert search(
        [
            {"id": "doc2", "text": "Is hex let a programmers site?"},
            {"id": "doc1", "text": "I am new hex let boy, dude"},
            {"id": "doc3", "text": "small cow says moooooo"},
        ],
        "hex",
    ) == ["doc2", "doc1"]


def test_only_one_match():
    assert search(
        [
            {"id": "doc2", "text": "Is green let a programmers site?"},
            {"id": "doc1", "text": "I am new hex let boy"},
            {"id": "doc3", "text": "small cow says moooooo"},
        ],
        "hex",
    ) == ["doc1"]


def test_search_no_match():
    assert (
        search(
            [
                {"id": "doc2", "text": "Is hexlet a programmers site?"},
                {"id": "doc1", "text": "I am new hexlet boy"},
                {"id": "doc3", "text": "small cow says moooooo"},
            ],
            "Duck",
        ) == []
    )


def test_search_with_punctuation():
    assert search(
        [
            {"id": "doc2", "text": "Is hex let a programmers site?"},
            {"id": "doc1", "text": "I am new ?hex? let ?boy?, dude"},
            {"id": "doc3", "text": "small cow says moooooo"},
        ],
        "hex!",
    ) == ["doc2", "doc1"]

    assert search(
        [
            {"id": "doc2", "text": "Is hex let a programmers site?"},
            {"id": "doc1", "text": "I am new ?hex? let ?boy?, dude"},
            {"id": "doc3", "text": "small cow says moooooo"},
        ],
        ";hex",
    ) == ["doc2", "doc1"]


def test_search_right_rank():
    doc1 = "I can't shoot straight unless I've had a pint!"
    doc2 = "Don't shoot shoot shoot that thing at me."
    doc3 = "I'm your shooter."

    docs = [
        {"id": "doc1", "text": doc1},
        {"id": "doc2", "text": doc2},
        {"id": "doc3", "text": doc3},
    ]

    assert search(docs, "shoot") == ["doc2", "doc1"]


def test_fuzzy_search():
    doc1 = "I can't shoot straight unless I've had a pint!"
    doc2 = "Don't shoot shoot shoot that thing at me."
    doc3 = "I'm your shooter."

    docs = [
        {"id": "doc1", "text": doc1},
        {"id": "doc2", "text": doc2},
        {"id": "doc3", "text": doc3},
    ]

    assert search(docs, "shoot at me") == ["doc2", "doc1"]

    doc1 = (
        "I can't shoot shoot shoot shoot shoot straight unless I've had a pint!"
    )
    doc2 = "Don't shoot that thing at me."
    doc3 = "I'm your shooter."

    docs = [
        {"id": "doc1", "text": doc1},
        {"id": "doc2", "text": doc2},
        {"id": "doc3", "text": doc3},
    ]

    assert search(docs, "shoot at me") == ["doc2", "doc1"]


def test_search_with_unknown_word():
    docs = [
        {
            "id": "doc1",
            "text": "I can't shoot straight unless I've had a pint!",
        },
        {"id": "doc2", "text": "Don't shoot shoot shoot that thing at me."},
        {"id": "doc3", "text": "I'm your shooter."},
    ]

    assert search(docs, "shoot at me, nerd") == ["doc2", "doc1"]
