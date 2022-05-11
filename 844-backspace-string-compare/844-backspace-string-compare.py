class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        li_s, li_t = list(s), list(t)
        
        return self.back(li_s) == self.back(li_t)
        
    def back(self, li):
        for i in range(len(li)-1):
            if "#" in li and li.index("#") == 0 : 
                li = li[1:]
                continue
            if "#" in li:
                li = li[:li.index("#")-1]+li[li.index("#")+1:]
        if len(li)>0 and li[-1] == "#":
            li = li[:-2]
        return li
        
        