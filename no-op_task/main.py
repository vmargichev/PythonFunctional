def markdown_to_text(doc_content):
    last = list(map(lambda x: x.lstrip('# '), doc_content.split('\n')))
    last2 = remove_asterix_from_words(last)
    return last2
def remove_asterix_from_words(doc_content_list):
    list2 = []
    list3 = []
    list4 = []
    string = ''
    for line in doc_content_list:
        list2.append(line.split(' '))
    for sublist in list2:
        sublist2 = []
        for value in sublist:
            if len(value) > 1:
                sublist2.append(value.strip('*'))
            else:
               sublist2.append(value) 
        list3.append(sublist2)
    for line in list3:
        list4.append(' '.join(line))
    return '\n'.join(list4)
