class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sent = sentence.split()
        dictionary.sort(key= lambda x : len(x))
        lens = [len(word) for word in dictionary]
        d = set(dictionary)

        for i, word in enumerate(sent):
            for n in lens:
                if word[:n] in d:
                    sent[i] = word[:n]
                    break
        
        res = ""
        for word in sent:
            res += word + " "
        res = res.rstrip()

        return res