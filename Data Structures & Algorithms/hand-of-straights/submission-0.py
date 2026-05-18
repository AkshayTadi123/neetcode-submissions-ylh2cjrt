class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        while hand:
            low = hand[0]
            hand.remove(low)
            for i in range(groupSize-1):
                if low+1 in hand:
                    hand.remove(low+1)
                    low += 1
                else:
                    return False

        return True