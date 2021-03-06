# coding=utf-8
import time

from game.mahjong.models.hutype.basetype import BaseType
from game.mahjong.constants.carddefine import CardType, CARD_SIZE
from game.mahjong.models.card.hand_card import HandCard
from game.mahjong.models.utils.cardanalyse import CardAnalyse


class BuQiuRen(BaseType):
    """
    2)	不求人：胡牌时，4副牌及将中没有吃牌、碰牌、明杠，自摸和牌。

    """

    def __init__(self):
        super(BuQiuRen, self).__init__()

    def is_this_type(self, hand_card, card_analyse):
        used_card_type = [CardType.WAN]  # 此游戏中使用的花色
        if len(hand_card.chi_card_vals) > 0:
            return False
        if len(hand_card.peng_card_vals) > 0:
            return False
        if len(hand_card.dian_gang_card_vals) > 0:
            return False
        return True


if __name__ == "__main__":
    pass
    card_analyse = CardAnalyse()
    hand_card = HandCard(0)
    # hand_card.hand_card_info = {
    #     1: [9, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 万
    #     2: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 条
    #     3: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 饼
    #     4: [2, 2, 0, 0, 0],                 # 风
    #     5: [3, 3, 0, 0],                    # 箭
    # }
    hand_card.hand_card_info = {
        1: [8, 0, 1, 1, 1, 1, 1, 1, 0, 2],  # 万
        2: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 条
        3: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 饼
        4: [3, 3, 0, 0, 0],                 # 风
        5: [0, 0, 0, 0],                    # 箭
    }

    hand_card.record_peng_card(17)
    hand_card.record_an_gang_card(18)
    hand_card.handle_hand_card_for_settle_show()
    hand_card.union_hand_card()
    print "hand_card =", hand_card.hand_card_vals
    test_type = BuQiuRen()
    start_time = time.time()
    print test_type.is_this_type(hand_card, card_analyse)
    print "time = ", time.time() - start_time