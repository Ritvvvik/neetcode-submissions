class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in mapp:
                mapp[sorted_word] = [word]
            else:
                mapp[sorted_word].append(word)
        result = []
        for item in mapp.values():
            result.append(item)
        return result

            

        