class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        birr = {5:0 , 10:0 , 20:0}
        inHand = 0
        for bill in bills:
            if bill == 5:
                birr[bill] += 1
                inHand += bill
            
            else:
                change = bill - 5
                if inHand >= change:
                    if change == 5:
                        if not birr[5]:
                            return False
                        birr[5] -= 1
                    else:
                        if birr[10] and birr[5]:
                            birr[10] -= 1
                            birr[5] -= 1
                        elif birr[5] >= 3:
                            birr[5] -= 3         
                        else:
                            return False
                    
                    inHand -= change
                    inHand += bill
                    birr[bill] += 1

                else:
                    return False

        return True
