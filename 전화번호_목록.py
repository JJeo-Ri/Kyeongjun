def solution(phone_book):
    answer = True #초깃값 True로 설정
    #반복문 통해 하나씩 확인
    for number in phone_book:
        sub_book = phone_book.copy() 
        sub_book.remove(number) #자기 자신은 제외하고 비교해야 하므로 sub_book 생성
        #반복문 통해 sub_book의 번호를 비교
        for sub_num in sub_book:
            #number가 다른 번호의 접두사가 되는 경우 answer을 False로 바꾸고 break
            if number in sub_num[:len(number)]:
                answer = False
                break
        if answer == False:
            break
    return answer
