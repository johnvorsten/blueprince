
# Python imports
import unittest

# Third party imports

# Local imports
from word_trie import TrieNode, Trie

# Declarations

#%%

class TestTrieNode(unittest.TestCase):
    
    def test_TrieNode_init(self):
        root = TrieNode('', None)
        child_a = TrieNode('a', root)
        child_n = TrieNode('n', child_a)
        child_t = TrieNode('t', child_n)
        
        # Set variables in a node like it was being assembled into a tree
        root.children['a'] = child_a
        child_a.children['n'] = child_n
        child_n.children['t'] = child_t
        
        self.assertEqual(root.data, '')
        self.assertEqual(child_a.data, 'a')
        self.assertEqual(child_n.data, 'n')
        self.assertEqual(child_t.data, 't')
        
        self.assertEqual(child_a.children['n'], child_n)
        self.assertEqual(child_n.children['t'], child_t)
        
        self.assertEqual(child_a.parent, root)
        self.assertEqual(child_n.parent, child_a)
        self.assertEqual(child_t.parent, child_n)
        self.assertEqual(len(child_t.children.items()), 0)
        
        return None
        
class TestTrie(unittest.TestCase):
    
    def test_Trie_init(self):
        
        tree = Trie()
        self.assertEqual(tree.root.data, '')
        self.assertEqual(len(tree.root.children.items()), 0)
        
        return None
        
    def test_Trie_insert(self):
        tree = Trie()
        word:str = 'ant'
        word_2 = 'antelope'
        word_3 = 'bomb'
        word_4 = 'bombastic'
        
        tree.insert_word(word)
        tree.insert_word(word_2)
        tree.insert_word(word_3)
        tree.insert_word(word_4)
        
    def test_Trie_search(self):
        tree = Trie()
        word:str = 'ant'
        word_2 = 'antelope'
        word_3 = 'bomb'
        word_4 = 'bombastic'
        
        tree.insert_word(word)
        tree.insert_word(word_2)
        tree.insert_word(word_3)
        tree.insert_word(word_4)
        
        self.assertEqual(tree.search_word('a')[0], False)
        self.assertEqual(tree.search_word('an')[0], False)
        self.assertEqual(tree.search_word('ant')[0], True)
        self.assertEqual(tree.search_word('ante')[0], False)
        self.assertEqual(tree.search_word('antel')[0], False)
        self.assertEqual(tree.search_word('antelo')[0], False)
        self.assertEqual(tree.search_word('antelop')[0], False)
        self.assertEqual(tree.search_word('antelope')[0], True)
        
        self.assertEqual(tree.search_word('b')[0], False)
        self.assertEqual(tree.search_word('bo')[0], False)
        self.assertEqual(tree.search_word('bom')[0], False)
        self.assertEqual(tree.search_word('bomb')[0], True)
        self.assertEqual(tree.search_word('bomba')[0], False)
        self.assertEqual(tree.search_word('bombas')[0], False)
        self.assertEqual(tree.search_word('bombast')[0], False)
        self.assertEqual(tree.search_word('bombasti')[0], False)
        self.assertEqual(tree.search_word('bombastic')[0], True)
        
        return None

if __name__ == '__main__':
    # testing
    unittest.main()