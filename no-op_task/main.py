def markdown_to_text(doc_content):
    last = list(map(lambda x: x.lstrip('# '), doc_content.split('\n')))
    last2 = remove_asterix_from_words(last)
    return last2

def remove_asterix_from_words(doc_content_list):
    for line in doc_content_list:
        words_in_line = line.split(' ')
        for word in words_in_line:
            if len(word) > 1 and '*' in word:
                word.strip('*')
                print(word)
    return '\n'.join(doc_content_list)
