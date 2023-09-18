class Solution:
    def minSteps(self, n: int) -> int:
        curr = 1
        clipboard = 0
        steps = 0

        while curr < n:
            if n % curr == 0:
                clipboard = curr
                steps += 1

            curr += clipboard
            steps += 1

        return steps


# top down solution 

class Solution:
    def minSteps(self, n: int) -> int:
        min_opp = {}
        def topDown(opp,screen,buffer):
            if screen == n:
                return 0
                
            if screen > n:
                return inf
            if (opp,screen,buffer) in min_opp:
                return min_opp[(opp,screen,buffer)]

            if opp == "C":
                min_opp[(opp,screen,buffer)] = 1 + topDown("P", screen, screen)
            else:
                paste_and_copy = 1 + topDown("C", screen + buffer, buffer)
                paste_and_paste = 1 + topDown("P", screen + buffer, buffer)
                min_opp[(opp,screen,buffer)] = min(paste_and_copy, paste_and_paste)

            return min_opp[(opp,screen,buffer)]

        return topDown("C", 1, 0)      
