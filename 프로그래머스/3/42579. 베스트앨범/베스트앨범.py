def solution(genres, plays):
    
    genre_dict = dict()

    #재생횟수 계산
    for i,g in enumerate(genres):
        if genre_dict.get(g) == None:
            genre_dict[g] = plays[i]
        else:
            genre_dict[g] += plays[i]
    
    #list 변환
    genre_dict = [[genre_dict[k],k] for k in genre_dict.keys()]
    
    genre_dict.sort(reverse=True)
    
    music_book = [[plays[i], i,genres[i]]for i in range(len(genres))]
    music_book.sort(key=lambda x:(-x[0],x[1]))

    result = []
    
    for _, genre in genre_dict:
        count = 0    
        for time,i,g in music_book:
            if count == 2:
                break
            if g == genre:
                count += 1
                result.append(i)
                
    return result