class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        returnList = []
        counter = 1

        for i in range(n):
            returnList.append(counter)
            if(counter * 10 <= n):
                counter*= 10
            elif (counter % 10 != 9 and counter + 1 <= n):
                counter+=1
            else:
                while(counter / 10) % 10 == 9:
                    counter/= 10
                counter = counter/10 + 1

        return returnList

        