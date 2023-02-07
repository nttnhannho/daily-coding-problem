"""
[Medium]

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""


class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()
        self.__suggestions = []

    def from_keys(self, keys):
        for key in keys:
            self.insert(key)

    def insert(self, key):
        node = self.root

        for k in key:
            if not node.children.get(k):
                node.children[k] = Node()
            node = node.children[k]

        node.is_end = True

    def get_suggestions(self, node, word):
        if node.is_end:
            self.__suggestions.append(word)

        for k, v in node.children.items():
            self.get_suggestions(v, word + k)

        return self.__suggestions

    def auto_suggest(self, key):
        node = self.root

        for k in key:
            if not node.children.get(k):
                return []
            node = node.children[k]

        if not node.children:
            return []

        return self.get_suggestions(node, key)


def main():
    query = "de"
    strings = ["dog", "deer", "deal"]

    trie = Trie()
    trie.from_keys(strings)

    print(trie.auto_suggest(query))


if __name__ == "__main__":
    main()
