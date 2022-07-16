class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        tem = float("inf")
        for i in range(len(list1)):
            if list1[i] in list2 and i+list2.index(list1[i]) < tem:
                tem = i+list2.index(list1[i])
                res = [list1[i]]
            elif list1[i] in list2 and i+list2.index(list1[i]) == tem:
                res.append(list1[i])
        return res