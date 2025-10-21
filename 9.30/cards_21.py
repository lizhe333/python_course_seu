import random

# 花色和点数
suits = ["♠", "♥", "♣", "♦"]
ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

def color_card(rank, suit):
    if suit in ["♥", "♦"]:
        return f"\033[31m{rank}{suit}\033[0m"  # 红色
    else:
        return f"\033[97m{rank}{suit}\033[0m"  # 高亮白色

# 随机抽 21 张牌
deck = random.sample([color_card(r, s) for s in suits for r in ranks], 24)

def show_columns(cards):
    cols = [cards[i::3] for i in range(3)]
    for i in range(7):
        print(f"{cols[0][i]:>4} {cols[1][i]:>4} {cols[2][i]:>4}")
    return cols

print("记住一张牌，我来找出它！")
for _ in range(3):
    cols = show_columns(deck)
    choice = int(input("你的牌在哪一列？(1/2/3): ")) - 1
    # 将选列放在中间
    deck = cols[(choice-1)%3] + cols[(choice)%3] + cols[(choice+1)%3]

print(f"你的牌是: {deck[10]}！")