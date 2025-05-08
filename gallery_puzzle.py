"""Gallery puzzle
"""

# Python imports
import nltk
import time
from typing import List
import random
import sys

# Third party imports

# Local imports
from word_trie import TrieNode, Trie

# Declarations
north_wall_line_1 = 'careahd'
north_wall_line_2 = 'sepiele'
north_wall_line_3 = 'viguitr'
north_wall_line_4 = 'poasunn'
north_wall_line_5 = 'fuottry'
north_wall_line_6 = 'rhcrras'
north_wall_line_7 = 'llmdleg'
north_wall_line_8 = 'hrtlhzh'

east_wall_line_1 = 'dafacnct'
east_wall_line_2 = 'genegley'
east_wall_line_3 = 'hisiltdh'
east_wall_line_4 = 'looonase'
east_wall_line_5 = 'mumuoets'
east_wall_line_6 = 'nhrprion'
east_wall_line_7 = 'rragsolr'
east_wall_line_8 = 'tyutthuk'

south_wall_line_1 = 'brodt'
south_wall_line_2 = 'wlucd'
south_wall_line_3 = 'fcrmk'
south_wall_line_4 = 'ponne'
south_wall_line_5 = 'tatrr'
south_wall_line_6 = 'shaas'
south_wall_line_7 = 'cieen'
south_wall_line_8 = 'deiia'

west_wall_line_1 = 'bavdan'
west_wall_line_2 = 'celted'
west_wall_line_3 = 'pirhog'
west_wall_line_4 = 'tonsnr'
west_wall_line_5 = 'lutilw'
west_wall_line_6 = 'shskrt'
west_wall_line_7 = 'mrovce'
west_wall_line_8 = 'wtiasy'

ENGLISH_WORDS = nltk.corpus.words.words()

FILEPATH_SAVE = './gallery_puzzle.txt'

#%%

def search_word_in_nltk_list(word:str) -> bool:
    """Example usage of checking if a string is in the list of english words
    ENGLISH_WORDS = nltk.corpus.words.words()
    'alphabet' in ENGLISH_WORDS
    """
    return word in ENGLISH_WORDS

def construct_word_trie():
    """Construct a word trie where all words are inserted into a Trie structure"""
    word_tree = Trie()
    
    for word in ENGLISH_WORDS:
        word_tree.insert_word(word)
        
    return word_tree

def main():

    # Construct the word trie
    word_trie = Trie()
    for word in ENGLISH_WORDS:
        word_trie.insert_word(word)

    # Puzzle north wall
    # 7 slots, 8 characters per slot
    matched_words:List[str] = []
    print("north puzzle")
    print(f"Starting search for {7**8} combinations of characters")
    slot_1 = [north_wall_line_1[0], north_wall_line_2[0], north_wall_line_3[0],
              north_wall_line_4[0], north_wall_line_5[0], north_wall_line_6[0],
              north_wall_line_7[0], north_wall_line_8[0]
              ]
    slot_2 = [north_wall_line_1[1], north_wall_line_2[1], north_wall_line_3[1],
              north_wall_line_4[1], north_wall_line_5[1], north_wall_line_6[1],
              north_wall_line_7[1], north_wall_line_8[1]
              ]
    slot_3 = [north_wall_line_1[2], north_wall_line_2[2], north_wall_line_3[2],
              north_wall_line_4[2], north_wall_line_5[2], north_wall_line_6[2],
              north_wall_line_7[2], north_wall_line_8[2]
              ]
    slot_4 = [north_wall_line_1[3], north_wall_line_2[3], north_wall_line_3[3],
              north_wall_line_4[3], north_wall_line_5[3], north_wall_line_6[3],
              north_wall_line_7[3], north_wall_line_8[3]
              ]
    slot_5 = [north_wall_line_1[4], north_wall_line_2[4], north_wall_line_3[4],
              north_wall_line_4[4], north_wall_line_5[4], north_wall_line_6[4],
              north_wall_line_7[4], north_wall_line_8[4]
              ]
    slot_6 = [north_wall_line_1[5], north_wall_line_2[5], north_wall_line_3[5],
              north_wall_line_4[5], north_wall_line_5[5], north_wall_line_6[5],
              north_wall_line_7[5], north_wall_line_8[5]
              ]
    slot_7 = [north_wall_line_1[6], north_wall_line_2[6], north_wall_line_3[6],
              north_wall_line_4[6], north_wall_line_5[6], north_wall_line_6[6],
              north_wall_line_7[6], north_wall_line_8[6]
              ]
    start_time = time.time()
    for char_1 in slot_1:
        for char_2 in slot_2:
            for char_3 in slot_3:
                for char_4 in slot_4:
                    for char_5 in slot_5:
                        for char_6 in slot_6:
                            for char_7 in slot_7:
                                word = char_1+char_2+char_3+char_4+char_5+char_6+char_7
                                found, node = word_trie.search_word(word)
                                if found:
                                    matched_words.append(word)
    end_time = time.time()
    print(f"Found {len(matched_words)} words in {end_time-start_time:0.2f} seconds")
    with open(FILEPATH_SAVE, 'wt', encoding='UTF-8') as file:
        file.write("North puzzle matched words:\n")
        file.write(f"Found {len(matched_words)} words in {end_time-start_time:0.2f} seconds\n")
        file.write(str(matched_words))
        file.write('\n\n')
    
    
    # Puzzle east wall
    # 8 slots, 8 characters per slot
    matched_words:List[str] = []
    print("east puzzle")
    print(f"Starting search for {8**8} combinations of characters")
    slot_1 = [east_wall_line_1[0], east_wall_line_2[0], east_wall_line_3[0],
              east_wall_line_4[0], east_wall_line_5[0], east_wall_line_6[0],
              east_wall_line_7[0], east_wall_line_8[0]
              ]
    slot_2 = [east_wall_line_1[1], east_wall_line_2[1], east_wall_line_3[1],
              east_wall_line_4[1], east_wall_line_5[1], east_wall_line_6[1],
              east_wall_line_7[1], east_wall_line_8[1]
              ]
    slot_3 = [east_wall_line_1[2], east_wall_line_2[2], east_wall_line_3[2],
              east_wall_line_4[2], east_wall_line_5[2], east_wall_line_6[2],
              east_wall_line_7[2], east_wall_line_8[2]
              ]
    slot_4 = [east_wall_line_1[3], east_wall_line_2[3], east_wall_line_3[3],
              east_wall_line_4[3], east_wall_line_5[3], east_wall_line_6[3],
              east_wall_line_7[3], east_wall_line_8[3]
              ]
    slot_5 = [east_wall_line_1[4], east_wall_line_2[4], east_wall_line_3[4],
              east_wall_line_4[4], east_wall_line_5[4], east_wall_line_6[4],
              east_wall_line_7[4], east_wall_line_8[4]
              ]
    slot_6 = [east_wall_line_1[5], east_wall_line_2[5], east_wall_line_3[5],
              east_wall_line_4[5], east_wall_line_5[5], east_wall_line_6[5],
              east_wall_line_7[5], east_wall_line_8[5]
              ]
    slot_7 = [east_wall_line_1[6], east_wall_line_2[6], east_wall_line_3[6],
              east_wall_line_4[6], east_wall_line_5[6], east_wall_line_6[6],
              east_wall_line_7[6], east_wall_line_8[6]
              ]
    slot_8 = [east_wall_line_1[7], east_wall_line_2[7], east_wall_line_3[7],
            east_wall_line_4[7], east_wall_line_5[7], east_wall_line_6[7],
            east_wall_line_7[7], east_wall_line_8[7]
            ]
    start_time = time.time()
    for char_1 in slot_1:
        for char_2 in slot_2:
            for char_3 in slot_3:
                for char_4 in slot_4:
                    for char_5 in slot_5:
                        for char_6 in slot_6:
                            for char_7 in slot_7:
                                for char_8 in slot_8:
                                    word = char_1+char_2+char_3+char_4+char_5+char_6+char_7+char_8
                                    found, node = word_trie.search_word(word)
                                    if found:
                                        matched_words.append(word)
    end_time = time.time()
    print(f"Found {len(matched_words)} words in {end_time-start_time:0.2f} seconds")
    with open(FILEPATH_SAVE, 'at', encoding='UTF-8') as file:
        file.write("East puzzle matched words:\n")
        file.write(f"Found {len(matched_words)} words in {end_time-start_time:0.2f} seconds\n")
        file.write(str(matched_words))
        file.write('\n\n')
    
    # Puzzle South wall
    # 5 slots, 8 characters per slot
    matched_words:List[str] = []
    print("south puzzle")
    print(f"Starting search for {5**8} combinations of characters")
    slot_1 = [south_wall_line_1[0], south_wall_line_2[0], south_wall_line_3[0],
              south_wall_line_4[0], south_wall_line_5[0], south_wall_line_6[0],
              south_wall_line_7[0], south_wall_line_8[0]
              ]
    slot_2 = [south_wall_line_1[1], south_wall_line_2[1], south_wall_line_3[1],
              south_wall_line_4[1], south_wall_line_5[1], south_wall_line_6[1],
              south_wall_line_7[1], south_wall_line_8[1]
              ]
    slot_3 = [south_wall_line_1[2], south_wall_line_2[2], south_wall_line_3[2],
              south_wall_line_4[2], south_wall_line_5[2], south_wall_line_6[2],
              south_wall_line_7[2], south_wall_line_8[2]
              ]
    slot_4 = [south_wall_line_1[3], south_wall_line_2[3], south_wall_line_3[3],
              south_wall_line_4[3], south_wall_line_5[3], south_wall_line_6[3],
              south_wall_line_7[3], south_wall_line_8[3]
              ]
    slot_5 = [south_wall_line_1[4], south_wall_line_2[4], south_wall_line_3[4],
              south_wall_line_4[4], south_wall_line_5[4], south_wall_line_6[4],
              south_wall_line_7[4], south_wall_line_8[4]
              ]
    start_time = time.time()
    for char_1 in slot_1:
        for char_2 in slot_2:
            for char_3 in slot_3:
                for char_4 in slot_4:
                    for char_5 in slot_5:
                        word = char_1+char_2+char_3+char_4+char_5
                        found, node = word_trie.search_word(word)
                        if found:
                            matched_words.append(word)
    end_time = time.time()
    print(f"Found {len(matched_words)} words in {end_time-start_time:0.2f} seconds")
    with open(FILEPATH_SAVE, 'at', encoding='UTF-8') as file:
        file.write("South puzzle matched words:\n")
        file.write(f"Found {len(matched_words)} words in {end_time-start_time:0.2f} seconds\n")
        file.write(str(matched_words))
        file.write('\n\n')
    
    
# Puzzle west wall
    # 6 slots, 8 characters per slot
    matched_words:List[str] = []
    print("West puzzle")
    print(f"Starting search for {6**8} combinations of characters")
    slot_1 = [west_wall_line_1[0], west_wall_line_2[0], west_wall_line_3[0],
              west_wall_line_4[0], west_wall_line_5[0], west_wall_line_6[0],
              west_wall_line_7[0], west_wall_line_8[0]
              ]
    slot_2 = [west_wall_line_1[1], west_wall_line_2[1], west_wall_line_3[1],
              west_wall_line_4[1], west_wall_line_5[1], west_wall_line_6[1],
              west_wall_line_7[1], west_wall_line_8[1]
              ]
    slot_3 = [west_wall_line_1[2], west_wall_line_2[2], west_wall_line_3[2],
              west_wall_line_4[2], west_wall_line_5[2], west_wall_line_6[2],
              west_wall_line_7[2], west_wall_line_8[2]
              ]
    slot_4 = [west_wall_line_1[3], west_wall_line_2[3], west_wall_line_3[3],
              west_wall_line_4[3], west_wall_line_5[3], west_wall_line_6[3],
              west_wall_line_7[3], west_wall_line_8[3]
              ]
    slot_5 = [west_wall_line_1[4], west_wall_line_2[4], west_wall_line_3[4],
              west_wall_line_4[4], west_wall_line_5[4], west_wall_line_6[4],
              west_wall_line_7[4], west_wall_line_8[4]
              ]
    slot_6 = [west_wall_line_1[5], west_wall_line_2[5], west_wall_line_3[5],
              west_wall_line_4[5], west_wall_line_5[5], west_wall_line_6[5],
              west_wall_line_7[5], west_wall_line_8[5]
              ]
    start_time = time.time()
    for char_1 in slot_1:
        for char_2 in slot_2:
            for char_3 in slot_3:
                for char_4 in slot_4:
                    for char_5 in slot_5:
                        for char_6 in slot_6:
                            word = char_1+char_2+char_3+char_4+char_5+char_6
                            found, node = word_trie.search_word(word)
                            if found:
                                matched_words.append(word)
    end_time = time.time()
    print(f"Found {len(matched_words)} words in {end_time-start_time:0.2f} seconds")
    with open(FILEPATH_SAVE, 'at', encoding='UTF-8') as file:
        file.write("West puzzle matched words:\n")
        file.write(f"Found {len(matched_words)} words in {end_time-start_time:0.2f} seconds\n")
        file.write(str(matched_words))
        file.write('\n\n')
    
    return None

def time_test_list_search():
    # First create a permutation of strings of various lengths
    # Each string is exactly 8 characters long, and each position within the string
    # Has exactly 8 possible characters it can be
    word_length:int = 8
    characters_per_slot:int = 8
    slot_1:List[str] = ['d','c','s','g','e','u','e','w']
    slot_2:List[str] = ['n','e','h','k','w','o','a','a']
    slot_3:List[str] = ['s','i','n','k','q','i','d','r']
    slot_4:List[str] = ['b','m','y','j','c','u','g','t']
    slot_5:List[str] = ['u','l','r','p','v','y','h','r']
    slot_6:List[str] = ['i','p','e','u','b','t','p','n']
    slot_7:List[str] = ['g','z','e','i','n','h','l','b']
    slot_8:List[str] = ['o','f','s','o','m','j','k','b']
    matched_words:List[str] = []
    print(f"Starting search for {word_length**characters_per_slot} combinations of characters")
    
    start_time = time.time()
    for char_1 in slot_1:
        for char_2 in slot_2:
            for char_3 in slot_3:
                for char_4 in slot_4:
                    for char_5 in slot_5:
                        for char_6 in slot_6:
                            for char_7 in slot_7:
                                for char_8 in slot_8:
                                    word = char_1+char_2+char_3+char_4+char_5+char_6+char_7+char_8
                                    if word in ENGLISH_WORDS:
                                        matched_words.append(word)
    end_time = time.time()
    
    print(f"Elapsed time: {end_time - start_time}")
    print(f"Found number of matched words: {len(matched_words)}")
    print(f"Found words: {matched_words}")
    
    return matched_words


def time_test_2():
    # First create a permutation of strings of various lengths
    # Each string is exactly 8 characters long, and each position within the string
    # Has exactly 8 possible characters it can be
    word_length:int = 4
    characters_per_slot:int = 4
    slot_1:List[str] = ['d','c','s','g','e','u','e','w']
    slot_2:List[str] = ['n','e','h','k','w','o','a','a']
    slot_3:List[str] = ['s','i','n','k','q','i','d','r']
    slot_4:List[str] = ['b','m','y','j','c','u','g','t']

    matched_words:List[str] = []
    print(f"Starting search for {word_length**characters_per_slot} combinations of characters")
    
    start_time = time.time()
    for char_1 in slot_1:
        for char_2 in slot_2:
            for char_3 in slot_3:
                for char_4 in slot_4:
                    word = char_1+char_2+char_3+char_4
                    if word in ENGLISH_WORDS:
                        matched_words.append(word)
    end_time = time.time()
    
    print(f"Elapsed time: {end_time - start_time}")
    print(f"Found number of matched words: {len(matched_words)}")
    print(f"Found words: {matched_words}")
    
    return matched_words

def time_test_construct_trie():
    """Test how much time it takes to insert words into the trie"""
    
    start_time = time.time()
    word_tree = Trie()
    for word in ENGLISH_WORDS[:1000]:
        word_tree.insert_word(word)
    end_time = time.time()
    print(f"This is now much time it takes to insert the first 1000 words into a Trie: {end_time - start_time:0.2f} seconds")
    
    start_time = time.time()
    for word in ENGLISH_WORDS[1000:10000]:
        word_tree.insert_word(word)
    end_time = time.time()
    print(f"This is now much time it takes to insert the next 9,000 words into the same Trie: {end_time - start_time:0.2f} seconds")

    start_time = time.time()
    word_tree = Trie()
    for word in ENGLISH_WORDS:
        word_tree.insert_word(word)
    end_time = time.time()
    print(f"This is now much time it takes to insert {len(ENGLISH_WORDS)} words into a Trie: {end_time - start_time:0.2f} seconds")
    
    return None

def time_test_search_trie():
    
    word_tree = Trie()
    for word in ENGLISH_WORDS:
        word_tree.insert_word(word)
        
    # Start searching for words in the tree
    random_words = random.sample(ENGLISH_WORDS, 1000)
    start_time = time.time()
    for word in random_words:
        found, node = word_tree.search_word(word)
        if not found:
            print(f"Didn't find this word {word}.... weird??")
        print(f"found word {word} at node {node.parent.data, node.data, node.word_end}")
    end_time = time.time()
    print(f"It took {end_time-start_time:0.2f} seconds to search through 1000 words")
    
    return None

if __name__ == '__main__':
    # time_test()
    # time_test_2()
    # time_test_construct_trie()
    # time_test_search_trie()
    main()
