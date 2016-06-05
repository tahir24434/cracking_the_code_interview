# Given a text file and a word, find the positions that the word occurs in the file. We'll be asked to find the
# positions of many words in the same file.
# http://www.ardendertat.com/2011/12/20/programming-interview-questions-23-find-word-positions-in-text/#sthash.TSPB2lvC.dpuf


# Will add position of a word inside text to the dictionary.
def build_index(text, word_pos_dict, pos=0):
    # Convert to list
    txt_lst = text.lower().split()
    for word in txt_lst:
        if word in word_pos_dict:
            word_pos_dict[word].append(pos)
        else:
            word_pos_dict[word] = [pos]
        pos += 1
    return pos


def find_word_positions(word, word_pos_dict):
    if word in word_pos_dict:
        return word_pos_dict[word]
    else:
        return None

pos = 0
word_pos_dict = dict()
txt_file = open('./sample_file', 'r')
for line in txt_file:
    pos = build_index(line, word_pos_dict, pos)

print (find_word_positions("apple", word_pos_dict))
