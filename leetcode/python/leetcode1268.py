class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()  ## sort

        answer = []
        for i in range(1, len(searchWord) + 1):
            prefix = searchWord[:i]
            append_arr = []
            count = 0
            for word in products:
                if word[:i] == prefix:
                    count += 1
                    append_arr.append(word)
                if count >= 3:
                    break
            answer.append(append_arr)
        return answer