print('연수생 여러분 안녕하세요!')
name = str(input('이름: '))
number = input('전화번호: ')
birth = input('생년월일: ')


print ('필기종목은 스포츠 심리학, 스포츠 교육학, 스포츠 사회학, 스포츠 윤리학, 한국체육사, 운동역학, 운동 생리학 총 7과목 있습니다. 이 중에서 5가지 선택하여 신청하시면 됩니다.')
subject = input ('필기 과목: ')
print (name + '님의 접수가 완료되었습니다. 필기시험일은 5월 4일입니다.')

print ('-----------------------------------------------------------------------------')
print (' 여러분의 필기합격을 응원합니다.')
print (' 필기는 5과목 합 300점 이상이 되어야 합격입니다.')
subject1 = int(input(' 과목1의 시험점수를 입력하세요.: '))
subject2 = int(input(' 과목2의 시험점수를 입력하세요.: '))
subject3 = int(input(' 과목3의 시험점수를 입력하세요.: '))
subject4 = int(input(' 과목4의 시험점수를 입력하세요.: '))
subject5 = int(input(' 과목5의 시험점수를 입력하세요.: '))
total = subject1+ subject2 +subject3+subject4+subject5
print ('총 점수는' + str(total) + '입니다.')
if total >= 300 :
    print ('축하드립니다. 합격입니다. 실기장에서 뵙겠습니다.')
    print ('-----------------------------------------------------------------------------')
    print (' 여러분의 실기합격을 응원합니다.')
    print (' 실기는 해당 기록별 점수가 상이합니다. 해당 연수원은 축구, 야구, 농구, 배구, 수영  종목 지정 기관입니다.')
    events = { '축구' : '칠월일일' , '야구' : '칠월이일' , '농구' : '칠월삼일', '배구':'칠월사일', '수영':'칠월오일'};
    myevent = input(str(list(events.keys())) + '중 시험 볼 종목은?: ')
    print('<%s> 종목 실기일자는 <%s> 입니다.' % (myevent, events[myevent]))
    print(' 연수생들은 모두 해당 종목별 실기일을 확인해주세요.')
else :
    print('합격점수 미만, 불합격입니다.')

if total >= 300 :  
    print ('-----------------------------------------------------------------------------')
    print ('입력예시 1분 40초의 경우 100초로 입력할 것.')
    record=int(input('실기 기록을 입력하세요.: '))

    if record < 85: 
        print ('60점입니다.')
        time = 60
    elif record <= 90:
        print (' 57점입니다.')
        time=57
    elif record <= 95:
        print (' 54점입니다.')
        time = 54
    elif record <= 98:
        print (' 51점입니다.')
        time = 51
    elif record <= 100:
        print (' 48점입니다.')
        time = 48
    else:
        print (' 합격점수 미만, 불합격입니다.')

    if record <= 100 :
        print (' 실기 자세 점수는 평가원이 직접 평가합니다.')
        position = int(input(' 평가원이 평가한 점수를 입력하세요. 40점 만점: '))

        def final (n1, n2):
            result = n1+n2
            return result

        result= final (int(time), int(position))
        print('총 점수는' + str(result) +'입니다.')
        if result >= 70 :
            print ('축하드립니다. 합격입니다. 8월 30일 실습연수기관에서 뵙겠습니다.')
        else:
            print (' 합격점수 미만, 불합격입니다.')
            
        print ('-----------------------------------------------------------------------------')

        if result >= 70:
            
            print (' 안녕하세요! 오늘은 해당종목 실습 연수일입니다. 기회 3번 이내에 연수 최저점수 이상 취득해야 자격증 발급이 가능하며 넘을 때까지 반복해야합니다.')
         

            for i in range (3):
                grade = int(input('연수 점수를 입력하세요 : '))
                if grade < 80:
                    print ('합격점수 미만 불합격입니다.')
                else :
                    print ('축하드립니다. 생활체육지도자 최종 합격자입니다.')
                    break
