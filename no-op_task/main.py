def markdown_to_text(doc_content):
    list_with_lstrip = list(map(lambda x: x.lstrip('# '), doc_content.split('\n')))
    return remove_asterix_from_words(list_with_lstrip)

def remove_asterix_from_words(doc_content_list):
    list_separate_word_line = []
    list_combine_words = []
    list_combine_lines = []
    for line in doc_content_list:
        list_separate_word_line.append(line.split(' '))
    for sublist in list_separate_word_line:
        new_sublist = []
        for value in sublist:
            if len(value) > 1:
                new_sublist.append(value.strip('*'))
            else:
               new_sublist.append(value) 
        list_combine_words.append(new_sublist)
    for line in list_combine_words:
        list_combine_lines.append(' '.join(line))
    return '\n'.join(list_combine_lines)
