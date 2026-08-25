class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        solution = []
        for s in strs:
            key = "".join(sorted(s))
            if (key in mydict):
                mydict[key].append(s)
            else:
                mydict[key] = [s]

        return list(mydict.values())        


        