def make_dict(sentences):
    word_global_count = {}
    word_sentence_count = {}

    for sentence in sentences:
        seen_in_sentence = set()  # To track words seen in this sentence
        
        for word in sentence.split():
            word_global_count[word] = word_global_count.get(word, 0) + 1
            # Track each word only once per sentence
            if word not in seen_in_sentence:
                word_sentence_count[word] = word_sentence_count.get(word, 0) + 1
                seen_in_sentence.add(word)
    
    return word_global_count, word_sentence_count


# Challenge 1
def uncommon_from_sentences(sentences):
    word_global_count, word_sentence_count = make_dict(sentences)

    result = []
    for word in word_global_count:
        if word_global_count[word] == 1 and word_sentence_count[word] == 1:
            result.append(word)

    return result
