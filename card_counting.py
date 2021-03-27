print("Start counting cards!")

def define_value(x):
    if x>=2 and x<=6:
        return 1
    elif x>=7 and x<=9:
        return 0
    elif (x>=10 and x<=13) or x==1:
        return -1
    
def calc_bet(t_c_main):
    t_c = round(t_c_main, 0)
    if t_c <= -2:
        return 0
    elif t_c == -1:
        return minimum_bet
    elif t_c == 0:
        return minimum_bet*2
    elif t_c ==1:
        return minimum_bet*4
    elif t_c == 2:
        return minimum_bet*8
    elif t_c == 3:
        return minimum_bet*12
    elif t_c >= 4:
        return minimum_bet*16
    
    
count = 0
true_count=0
decks = 6
soft_17 = False
number_of_cards = decks*52
card_counter = 0
#idea 1-12 aggresive spread seat --> implement other day
minimum_bet = 5 #recommender bankroll 5.000 
flag = True
while True:
    card = 0
    flag = True
    try:
        card = int(input())
    except Exception as e:
        flag = False
    while card <=0 or card >13 or flag == False:
        flag = True
        print("Wrong card, enter it again")
        try:
            card = int(input())
        except Exception as e:
            flag = False
    card_counter = card_counter +1
    value = define_value(card)
    count = count+value
    print("Card value: "+str(value)+" and count : "+str(count))
    true_count = count / ((number_of_cards - card_counter)/52)
    print("The true count is : "+str(true_count))
    print("The rounded up true count is : "+str(round(true_count,0)))
    x = true_count -1
    adv = x * 0.5
    print("Players advantage : "+str(adv)+"%")
    print("Recommender bet : "+str(calc_bet(true_count)))
    