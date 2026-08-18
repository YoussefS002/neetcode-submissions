class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        after={}
        for word in words:
            for c in word:
                after[c]=[]
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
            idx=0
            while idx<len(word1) and idx<len(word2) and word1[idx]==word2[idx]:
                idx+=1
            if idx<len(word1) and idx==len(word2):
                return ""
            if idx<len(word1) and idx<len(word2):
                letter1=word1[idx]
                letter2=word2[idx]
                if letter2 not in after[letter1]:
                    after[letter1].append(letter2)
        # detect cycles
        GRAY, BLACK = 1, 2
        color={}
        def detect_cycle(node):
            color[node]=GRAY
            for ng in after[node]:
                if ng in color:
                    if color[ng]==GRAY:
                        return True
                else:
                    if detect_cycle(ng):
                        return True
            color[node]=BLACK
            return False
        for node in after:
            if node not in color:
                if detect_cycle(node):
                    return ""
        order=[]
        vis=set()
        def topological_sort(node):
            if node in vis:
                return
            vis.add(node)
            for ng in after[node]:
                topological_sort(ng)
            order.append(node)
        for node in after:
            topological_sort(node)
        return "".join(order[::-1])
        