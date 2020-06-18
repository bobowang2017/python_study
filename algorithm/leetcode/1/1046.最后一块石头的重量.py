# -*- coding: utf-8 -*-
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        def merge(_stones):
            stone_1, stone_2 = _stones[0], _stones[1]
            _res = abs(stone_1 - stone_2)
            if _res != 0:
                insert_tag = False
                for i in range(2, len(_stones)):
                    if _stones[i] > _res:
                        continue
                    else:
                        insert_tag = True
                        _stones.insert(i, _res)
                        break
                if not insert_tag:
                    _stones.append(_res)
            return _stones[2:]

        if len(stones) == 1:
            return stones[0]
        if len(stones) == 2:
            return abs(stones[0] - stones[1])
        stones = sorted(stones, reverse=True)
        while len(stones) > 2:
            stones = merge(stones)
        if len(stones) == 2:
            return abs(stones[0] - stones[1])
        elif len(stones) == 1:
            return stones[0]
        else:
            return 0


s = Solution()
res = s.lastStoneWeight([3,7,8])
print(res)
