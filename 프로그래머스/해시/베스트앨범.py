def solution(genres, plays):
    genre_sum={}
    genre_songs={}
    for i in range(len(genres)):
        g=genres[i]
        p=plays[i]
        if g not in genre_sum:
            genre_sum[g]=0
            genre_songs[g]=[]
        genre_sum[g]+=p
        genre_songs[g].append((p,i))
    
    genre_list=[]
    for k, v in genre_sum.items():
        genre_list.append((v,k))
    genre_list.sort(reverse=True)

    answer = []
    for total, g in genre_list:
        temp=[]
        for p,idx in genre_songs[g]:
            temp.append((-p,idx))

        temp.sort()
        for i in range(min(2,len(temp))):
            answer.append(temp[i][1])
    return answer


# def solution(genres, plays):
#     answer = []

#     dic1 = {}
#     dic2 = {}

#     for i, (g, p) in enumerate(zip(genres, plays)):
#         if g not in dic1:
#             dic1[g] = [(i, p)]
#         else:
#             dic1[g].append((i, p))

#         if g not in dic2:
#             dic2[g] = p
#         else:
#             dic2[g] += p

#     for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
#         for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
#             answer.append(i)

#     return answer
