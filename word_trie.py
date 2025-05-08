"""A Trie which allows for efficient searching for english words"""

# Python imports
from typing import Dict, Type, Union, Tuple

# Third party imports

# Local imports

# Declarations

#%%

class TrieNode:
    """A node within a Trie
    Class instance members
        data: A string character which represents what character is stored in this node
        parent: A reference to another Trie node which is the parent of this Trie node
        children: A dictionary of [string, child]"""
    
    
    def __init__(self, character:str, parent:Union[None, Type['TrieNode']]) -> None:
        """Initialize a tree node. Each node contains a character, a reference to its parent, and 
        a dictionary containing its children"""
        
        self.data = character
        self.parent = parent
        self.children:Dict[str, TrieNode] = {}
        # A full word is formed by the concatenation of the node and its parents
        # But not every node that has parents forms a word
        # For example, the word 'ant' is a word
        # The word 'antelope' is also a word
        # The characters 'antel' is not a word even though it exists in a Trie
        # If this node forms the end of a word then keep track of it
        self.word_end:bool = False 
        
        return None

class Trie:
    
    def __init__(self):
        self.root = TrieNode('', None) # The root of a tree is a node which contains an empty string
        return None
    
    def insert_word(self, word:str) -> TrieNode:
        """Insert a string into the Trie
        Return the last node of the word within the tree"""
        
        # Loop through each character
        character:str
        node = self.root
        for character in word:
            try:
                # See if the node already has the character stored as a child
                # If the node already exists, then update the next node to be the child
                node = node.children[character]
                
            except KeyError:
                # if the node does not exist then create it
                node.children[character] = TrieNode(character, node) # The parent of the new node is the current node
                node = node.children[character]
        
        # A full word is formed by the concatenation of the node and its parents
        # But not every node that has parents forms a word
        # For example, the word 'ant' is a word
        # The word 'antelope' is also a word
        # The characters 'antel' is not a word even though it exists in a Trie
        # If this node forms the end of a word then keep track of it
        node.word_end = True
        return node
    
    def search_word(self, word:str) -> Tuple[bool, TrieNode]:
        """Search if a string exists within the tree
        Return the last node that corresponds to the last character of the string"""
        node = self.root
        for character in word:
            try:
                # See if the node already has the character stored as a child
                node = node.children[character]
                
            except KeyError:
                # if the node does not exist then return false
                return False, None
            
        # The node exists only if it is a node and it forms the end of a word
        if node.word_end:
            return True, node
        
        return False, None
    
    def remove(self):
        raise NotImplementedError

