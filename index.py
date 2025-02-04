import os, random, time
from wonderwords import RandomWord
from rich.tree import Tree
from rich import print as RichP


def get_list_of_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

words = get_list_of_words('word.txt')





class Enderecos:

    def __init__(self):
        self.ip = f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(10, 99)}"
        self.dificulty = random.randint(1, 5)
        self.passwordWords = []
        self.password = ""
        self.rewards = int(random.randint((300 * self.dificulty), (2000 * self.dificulty)) * 1.33)
        self.complete = False
        for x in range(1, 2 * self.dificulty):
            random_word = random.choice(words)
            self.passwordWords.append(random_word)
            self.password = f"{self.password}{random_word}"
        # print(f"IP: {self.ip}\nDificulty: {self.dificulty}\nList Words: {self.passwordWords}\nPassword: {self.password}\nRewards: {self.rewards}")

    def getIp(self):
        return self.ip
    
    def getDificulty(self):
        return self.dificulty
    
    def getPasswordWords(self):
        return self.passwordWords
    
    def getPassword(self):
        return self.password
    
    def getRewards(self):
        return self.rewards
    
    def getComplete(self):
        return self.complete
    


a = Enderecos()

from rich.tree import Tree
from rich import print

tree = Tree("👾 [red]Player Status")
tree.add(f"Cash: {a.getIp()}")
tree.add("bar")
baz_tree = tree.add("baz")



print(tree)