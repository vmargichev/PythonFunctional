def word_count_memo(document, memos):
    memos_copy = memos.copy()
    document_count = word_count(document)
    if document not in memos_copy:
        memos_copy[document] = document_count
    return  memos_copy[document], memos_copy


# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count
