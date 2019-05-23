class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

    def all_words(self, prefix):
        if self.end:
            yield prefix

        for letter, child in self.children.items():
            yield child.all_words(prefix + letter)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            node = current.children.get(letter)
            if not node:
                node = TrieNode()
                current.children[letter] = node
            current = node
        current.end = True
        
    def all_words_beginning_with_prefix(self, prefix):
        current = self.root
        for c in prefix:
            current = current.children.get(c)
            if current is None:
                return
        yield current.all_words(prefix)




# class TrieNode:
#     def __init__(self):
#         self.end = False
#         self.children = {}

#     def all_words(self, prefix):
#         if self.end:
#             yield prefix

#         for letter, child in self.children.items():
#             yield child.all_words(letter + prefix)


# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def all_words_beginning_with_prefix(self, prefix):
#         curr = self.root
#         for c in prefix:
#             curr = curr.children.get(c)
#             if curr is None:
#                 return
#             yield cur.all_words(prefix)

trie = Trie()
trie.insert('foobar')
trie.insert('foo')
trie.insert('bar')
trie.insert('foob')
trie.insert('foof')

print(list(trie.all_words_beginning_with_prefix('foo')))