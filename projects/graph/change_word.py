"""
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest
transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.
"""
from graph import Graph


def change_word(begin_word, end_word):
    g = Graph()
    with open('words.txt') as f:
        words = f.read().split("\n")

    words.append(begin_word)
    for word in words:
        g.add_vertex(word)

    lengths = [len(word) for word in words]
    max_length = max(lengths)
    divide_by_length = [None] * max_length
    for word in words:
        l = len(word)
        if divide_by_length[l-1] is None:
            divide_by_length[l-1] = [word]
        else:
            divide_by_length[l-1].append(word)

    for word_arr in divide_by_length:
        storage = set()
        for word1 in word_arr:
            storage.add(word1)
            for word2 in word_arr:
                if word2 not in storage:
                    for i in range(len(word1)):
                        letter1 = word1[i]
                        letter2 = word2[i]
                        if word1.split(letter1) == word2.split(letter2):
                            g.add_edge(word1, word2)
                            g.add_edge(word2, word1)
                            break
        print('finished adding edges for one length array')

    return g.bfs(begin_word, end_word)

# Group:
# Jason Loomis
# Jackson McComas
# Ryan State
# David Nagy