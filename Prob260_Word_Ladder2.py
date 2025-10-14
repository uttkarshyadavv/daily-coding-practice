from collections import deque
def ladder(start,wordlist,end):
    wordset=set(wordlist)
    if end not in wordset:
        return []
    result=[]
    queue=deque()
    queue.append([start])
    while len(queue)!=0:
        level_size=len(queue)
        chosen_words= set()
        for _ in range(level_size):
            sequence=queue.popleft()
            last_word= sequence[-1]
            if last_word==end:
                result.append(sequence)
                continue
            for i in range(len(last_word)):
                for ch in "qwertyuiopasdfghjklxcvbnm":
                    if ch == last_word[i]:
                        continue
                    new_word= last_word[:i] + ch + last_word[i+1:]
                    if new_word in wordset:
                        new_seq= sequence+ [new_word]
                        queue.append(new_seq)
                        chosen_words.add(new_word)
        for words in chosen_words:
            wordset.remove(words)
    return result

