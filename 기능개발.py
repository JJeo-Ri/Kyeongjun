def solution(progresses, speeds):
    days = []
    #각 기능 개발에 걸리는 시간(day) 리스트 만들기
    for i, progress, speed in zip(range(len(progresses)), progresses, speeds):
        if (100-progress) % speed == 0:
            days.append((100-progress)//speed)
        else:
            days.append((100-progress)//speed+1)
    
    results = [] #최종결과 리스트
    result = 1 #동일한 날 배포되는 기능의 수
    pivot = days[0] #기준점(개발이 지연되고 있는 기능)
    #for문을 돌며 pivot보다 작으면(즉, 개발 완성 후 배포를 기다리는 중이면) result에 1을 더해준다.
    for day in days[1:]:
        if pivot > day:
            result += 1
        #pivot보다 크면(pivot의 배포 완료 후 개발 시간이 더 오래 걸리는 기능 대기중이면)     
        else:
            results.append(result) #배포한 결과들은 results에 추가
            result = 1 #result는 초기화
            pivot = day #pivot을 바꿔준다
    results.append(result) #마지막에 마무리되는 기능들도 results에 추가
    return results
