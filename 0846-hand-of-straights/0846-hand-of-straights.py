class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        n = len(hand)
        if n % groupSize :
            return False
        hmap = {}
        for i in hand:
            hmap[i] = hmap.get(i,0) + 1

        for card in sorted(hmap):
            if hmap[card] > 0:
                count = hmap[card]    
                for j in range(card,card+groupSize):
                    if hmap.get(j,0) < count:
                        return False
                    hmap[j] = hmap[j] - count
        return True                

            
        