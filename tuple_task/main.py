def add_doc(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    new_doc_2 = documents + (new_doc,)
    return new_doc_2
