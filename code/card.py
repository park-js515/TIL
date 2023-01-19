# 카드 생성
def making_card_list() -> list:
	card_list = []

	for shape in ["spade", "heart", "diamond", "clover"]:

		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:

			card_list.append((shape, number))

	return card_list


trump_card_list = making_card_list()

# 셔플하기
import random

random.shuffle(trump_card_list)
print(trump_card_list)

# 누가 이기는지 정하기
def compare_cards(p1, p2):
    
    def val(pattern):
        if (pattern == "clover"):
            return 0
        elif (pattern == "heart"):
            return 1
        elif (pattern == "diamond"):
            return 2
        else:
            return 3
    
    def val2(pattern):
     
        if (pattern == 'A'):
            return 14
        elif (pattern == 'J'):
            return 11
        elif (pattern == 'Q'):
            return 12
        elif (pattern == 'K'):
            return 13
        else:
            return pattern


    p11 = (val(p1[0]), val2(p1[1]))
    p21 = (val(p2[0]), val2(p2[1]))
    lst = [p11, p21]
    res = sorted(lst, key = lambda x: (x[1],x[0]), reverse = True)
    
    if (res[0] == p11):
        return 1
    else:
        return 2

# 6번 이길 때까지 시행하고, 결과 출력하기
p1_score = 0
p2_score = 0

while (p1_score < 6 and p2_score < 6):
    p1 = trump_card_list.pop(0)
    p2 = trump_card_list.pop(0)

    result = compare_cards(p1, p2)

    if (result == 1):
        p1_score += 1
        print(p1, p2, "player1 win!")
    else:
        p2_score += 1
        print(p1, p2, "player2 win!")
    
if (p1_score > p2_score):
    print(f"{p1_score}:{p2_score} Finally player1 win")
else:
    print(f"{p1_score}:{p2_score} Finally player2 win")
