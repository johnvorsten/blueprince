"""Gallery puzzle
"""

# Python imports
import nltk
import time
from typing import List

# Third party imports

# Local imports

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

#%%

def check_word(word:str) -> bool:
    """Example usage of checking if a string is in the list of english words
    ENGLISH_WORDS = nltk.corpus.words.words()
    'alphabet' in ENGLISH_WORDS
    """
    return word in nltk.corpus.words.words()

def main():

    return None

def time_test():
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

if __name__ == '__main__':
    print(time_test_2())
