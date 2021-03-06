# coding=utf-8
import time

from game.mahjong.models.hutype.basetype import BaseType
from game.mahjong.constants.carddefine import CardType, CARD_SIZE
from game.mahjong.models.card.hand_card import HandCard
from game.mahjong.models.card.card import Card
from game.mahjong.models.utils.cardanalyse import CardAnalyse


class ShuangMingGang(BaseType):
    """
    3)	双明杠：胡牌时，牌里有2个明杠。
    """

    def __init__(self):
        super(ShuangMingGang, self).__init__()

    def is_this_type(self, hand_card, card_analyse):
        used_card_type = [CardType.WAN]  # 此游戏中使用的花色
        return (len(hand_card.bu_gang_card_vals)+len(hand_card.dian_gang_card_vals)) == 2



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
        1: [14, 4, 4, 4, 0, 0, 0, 0, 0, 2],  # 万
        2: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 条
        3: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 饼
        4: [0, 0, 0, 0, 0],                 # 风
        5: [0, 0, 0, 0],                    # 箭

    }
    hand_card.handle_hand_card_for_settle_show()
    hand_card.union_hand_card()
    print "hand_card =", hand_card.hand_card_vals
    test_type = ShuangMingGang()
    start_time = time.time()
    print test_type.is_this_type(hand_card, card_analyse)
    print "time = ", time.time() - start_time