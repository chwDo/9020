import sys
res = []
def count_8_to_10(current_hour,current_minute,arrive_minute,arrive_hour ):
    n_o_p = 0
    if current_hour >=10:
        return 0
    if current_hour < 8:
        current_hour = 8
        current_minute = 0
    if arrive_hour >=10:
        arrive_hour = 10
        arrive_minute = 0
    n_o_p += (arrive_hour - current_hour) * 60 + arrive_minute - current_minute
    return n_o_p * 3
def count_12_to_14(current_hour,current_minute,arrive_minute,arrive_hour ):
    n_o_p = 0
    if current_hour >=14:
        return 0
    if current_hour < 12:
        current_hour = 12
        current_minute = 0
    if arrive_hour >= 14:
        arrive_hour = 14
        arrive_minute = 0
    n_o_p += (arrive_hour - current_hour) * 60 + arrive_minute - current_minute
    return n_o_p * 10
def conut_18_to_20(current_hour,current_minute,arrive_minute,arrive_hour ):
    n_o_p = 0
    if current_hour >=20:
        return 0
    if current_hour < 18:
        current_hour = 18
        current_minute = 0
    if arrive_hour >= 20:
        arrive_hour = 20
        arrive_minute = 0
    n_o_p += (arrive_hour - current_hour) * 60 + arrive_minute - current_minute
    return n_o_p * 20

def count_10_to_12(current_hour,current_minute,arrive_minute,arrive_hour ):
    n_o_p = 0
    if current_hour >=12:
        return 0
    if current_hour < 10:
        current_hour = 10
        current_minute = 0
    if arrive_hour >=12:
        arrive_hour = 12
        arrive_minute = 0
    n_o_p += (arrive_hour - current_hour) * 60 + arrive_minute - current_minute
    return n_o_p / 5

def count_14_to_18(current_hour,current_minute,arrive_minute,arrive_hour ):
    n_o_p = 0
    if current_hour >=14:
        return 0
    if current_hour < 14:
        current_hour = 14
        current_minute = 0
    if arrive_hour >=18:
        arrive_hour = 18
        arrive_minute = 0
    n_o_p += (arrive_hour - current_hour) * 60 + arrive_minute - current_minute
    return n_o_p / 5


def test_time(current_hour,current_minute,aim_hour,aim_minute,travel_time,n_o_p):
    arrive_minute,arrive_hour = (current_minute + travel_time) % 60, current_hour + (current_minute + travel_time) / 60
    n_o_p = count_8_to_10(current_hour,current_minute,arrive_minute,arrive_hour )+count_10_to_12(current_hour,current_minute,arrive_minute,arrive_hour )+ \
    count_12_to_14(current_hour, current_minute, arrive_minute, arrive_hour) + count_14_to_18(current_hour, current_minute, arrive_minute, arrive_hour) +\
    conut_18_to_20(current_hour, current_minute, arrive_minute, arrive_hour)
    if arrive_hour < aim_hour and arrive_minute < aim_minute:
        return n_o_p + travel_time
    else:
        return -1
    





def solution(current_hour,current_minute,aim_hour,aim_minute,idd,distance,number_of_people):
    time = test_time(current_hour,current_minute,distance * 10,number_of_people)
    cost = distance * 10
    
    
    res.append()

if __name__ == "__main__":
    current_hour,current_minute = sys.stdin.readline().split()
    aim_hour,aim_minute = sys.stdin.readline().split()
    nums = int(sys.stdin.readline())
    for i in range(nums):
        idd,distance,number_of_people = sys.stdin.readline().split()
        solution(int(current_hour),int(current_minute),int(aim_hour),int(aim_minute),int(idd),int(distance),int(number_of_people))




