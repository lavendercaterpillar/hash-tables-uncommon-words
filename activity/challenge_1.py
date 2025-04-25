# def make_dict(words_of_sentences):

#     make_dict = {}
#     for word in words_of_sentences:
#         if word not in words_of_sentences:
#             make_dict[word] = 1
#         else:
#             make_dict[word] += 1

#     return make_dict


# def uncommon_from_sentences(sentences):

#     words_of_sentences = []
    
#     for i in range(len(sentences)):
#         words_of_sentences += (sentences[i].split())
    
#     allwords_dict = make_dict(words_of_sentences)  

#     result = []
#     for word, frequency in allwords_dict:
#         if frequency == 1 and word not in result:
#             result.append(word)

#     return result          

#  --------------------- Second Solution ------------------
def make_dict(sentences):
    word_global_count = {}
    word_sentence_count = {}

    for sentence in sentences:
        seen_in_sentence = set()
        word_count = {}
        
        for word in sentence.split():
            word_count[word] = word_count.get(word, 0) + 1
        
        for word, count in word_count.items():
            word_global_count[word] = word_global_count.get(word, 0) + count
            if word not in seen_in_sentence:
                word_sentence_count[word] = word_sentence_count.get(word, 0) + 1
                seen_in_sentence.add(word)
    
    return word_global_count, word_sentence_count

# Challenge 1
# def uncommon_from_sentences(sentences):
#     word_global_count, word_sentence_count = make_dict(sentences)

#     result = []
#     for word in word_global_count:
#         if word_global_count[word] == 1 and word_sentence_count[word] == 1:
#             result.append(word)

#     return result

# Challenge 2
def uncommon_from_sentences(sentences):
    word_global_count, word_sentence_count = make_dict(sentences)

    result = []
    for word in word_global_count:
        if word_global_count[word] >= 1 and word_sentence_count[word] == 1:
            result.append(word)

    return result
