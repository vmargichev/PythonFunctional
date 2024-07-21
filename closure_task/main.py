def word_count_aggregator():
    word_count = 0
    def word_counter(input):
        nonlocal word_count
        list_input = input.split(' ')
        word_count += len(list_input)
        return word_count
    return word_counter
