# Challenge 2
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

def uncommon_from_sentences(sentences):
    word_global_count, word_sentence_count = make_dict(sentences)

    result = []
    for word in word_global_count:
        # A word is uncommon if:
        # 1. It appears exactly once in total (word_global_count[word] == 1)
        # 2. It appears multiple times in one sentence but not in any other sentence (word_sentence_count[word] == 1)
        if word_global_count[word] == 1 or word_sentence_count[word] == 1:
            result.append(word)

    return result
