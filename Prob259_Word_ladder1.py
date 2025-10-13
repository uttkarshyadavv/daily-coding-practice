#BFS
from collections import deque
def word(start,wordlist,end):
    set1=set(wordlist)
    if end not in set1:
        return 0
    queue=deque()
    queue.append((start,1))
    while len(queue)!=0:
        curr_word,level=queue.popleft()
        if curr_word == end:
            return level
        for i in range(len(curr_word)):
            for ch in "qwertyuiopasdfghjklzxcvbnm":
                if ch==curr_word[i]:
                    continue
                new_word=curr_word[:i]+ch+curr_word[i+1:]
                if new_word in set1:
                    queue.append((new_word,level+1))
                    set1.remove(new_word)
    return 0


        
