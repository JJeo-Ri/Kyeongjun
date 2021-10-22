def solution(board, moves):
    answer = 0 
    pocket = []

    #moves가 빈 리스트가 될 때까지 반복
    while moves:
        pick = moves.pop(0)-1 #인형을 뽑을 공간
        for i in range(len(board)):
            doll = board[i][pick] #뽑은 인형의 번호
            if doll != 0: #인형이 있는 곳 찾으면 진행
                board[i][pick] = 0 #뽑은 인형은 보드에서 제거
                #pocket에 인형이 없을 경우 doll 추가
                if len(pocket) == 0:
                    pocket.append(doll)
                #pocket에 인형이 있을 경우 
                else:
                    #이전 인형과 같으면 제거하고 answer에 +2
                    if pocket[-1] == doll:
                        pocket.pop()
                        answer += 2
                    #다르면 doll 추가
                    else:
                        pocket.append(doll)
                break
    return answer
