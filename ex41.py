import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
      "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
      "Set *** to an instance of class %%%",
    "***.***(@@@)":
      "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'"
}

#do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    #print(word)
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in 
                   random.sample(WORDS, snippet.count("%%%"))]
    #Chooses k unique random elements from a population sequence or set.
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
    #返回范围[a, b]的随机整数，包括两个端点。  
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))
    
    for sentence in snippet, phrase:
        result = sentence[:]

        #fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)
        
        #fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        #fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
    #print(">>>>>results:", results)
    return results

#keep going until they hit CTRL-D
try:
    while True:
        #将字典PHRANSES的key赋值给snippets
        snippets = list(PHRASES.keys())
        #将列表x移到适当位置，并返回None。
        random.shuffle(snippets)

        for snippet in snippets:
            #从字典中取value
            phrase = PHRASES[snippet]
            #对每一个key和value进行操作，替换%%%，***，@@@
            question, answer = convert(snippet, phrase)
            
            if PHRASES_FIRST:
                question, answer = answer, question
            
            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")



