def caculate_x_plus(L):
    if 'a' not in L:
        return False
    x_plus = set(L)
    while 1:
        flag = 0
        for i in F:
            if i in L:
                for values in F[i]:
                    if values not in x_plus:
                        flag = 1
                        x_plus.add(values)
                        L = ''.join(x_plus)
        if flag == 0:
            if len(x_plus) == 8:
                return True
            else:
                return False


def caculate_candidate_keys(s):
    # print('answer', answer_list)
    state = False
    for i in s:
        s.remove(i)
        c = ''.join(s)
        t_state = caculate_x_plus(c)
        state = state | t_state
        if t_state:
            global counter, counter_set
            if s not in counter_set:
                counter_set.append(s.copy())
                counter += 1
            caculate_candidate_keys(s.copy())
        s.append(i)
        s.sort()
    if not state:
        if s not in answer_list:
            answer_list.append(s.copy())
    return


R = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i']
F = {'b': 'ch', 'bcd': 'hi', 'ei': 'h', 'h': 'ab', 'i': 'e'}
answer_list = []
L = 'abcdeghi'
LL = [i for i in L]
counter_set = [R]
counter = 0
s = set()
print(caculate_x_plus('dig'))
caculate_candidate_keys(LL)
print(answer_list)
# counter_set.sort()
# for i in counter_set:
#     print(i)
# print(counter + 1)

# 01 背包问题
# d = {0:(3, 7), 1: (4,10), 2:(7, 15)}
# n = 3
# dp = [0]*11
# for i in range(0,n):
#     if i ==0:
#         for j in range(1,11):
#             if j >= d[i][0]:
#                 dp[j] = d[i][1]
#         print(dp)
#     else:
#         for j in range(10,d[i][0]-1,-1):
#             dp[j] = max(dp[j], dp[j-d[i][0]]+d[i][1])
#         print(dp)
# print(dp[1:])

# 完全 背包问题
# d = {0:(3, 7), 1: (4,10), 2:(7, 15)}
# n = 3
# dp = [0]*11
# for i in range(0,n):
#         for j in range(d[i][0],11):
#             dp[j] = max(dp[j], dp[j-d[i][0]]+d[i][1])
#         print(dp)
# print(dp[1:])
#
# void completePack(int dp[],int value,int weight,int total)
# {
#     int i;
#     for(i=weight;i<=total;i++)
#     {
#         dp[i]=max(dp[i],dp[i-weight]+value);
#     }
# }
#
# void ZeroOnePack(int dp[],int value,int weight,int total)
# {
#     int i;
#     for(i=total;i>=weight;i--)
#     {
#         dp[i]=max(dp[i],dp[i-weight]+value);
#     }
# }
#
#
# //多重背包问题 优化 一维数组 二进制的思想  时间复杂度为O(V*Σlog n[i])
# void mutiPack(int dp[],int value,int weight,int amount,int total)
# {
#     if(weight*amount>total)
#     {
#         completePack(dp,value,weight,total);
#     }
#     else
#     {
#         int k=1;
#         while(amount-k>=0)
#         {
#             ZeroOnePack(dp,k*value,k*weight,total);
#             amount-=k;
#             k*=2;
#         }
#         ZeroOnePack(dp,amount*value,amount*weight,total);
#     }
# }
#
#
# int main()
# {
#     int n,w;
#     cin>>n>>w;
#     int i;
#     int wi,vi,ci;
#     for(i=0;i<n;i++)
#     {
#         cin>>wi>>vi>>ci;
#         mutiPack(dp_1,vi,wi,ci,w);
#     }
#
#     cout<<dp_1[w]<<endl;
#     return 0;
# }
