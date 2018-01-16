#MyMagic8Ball

import random

#답변을 입력해 봅시다
ans1=
ans2=
ans3=
ans4=
ans5=
ans6=
ans7=
ans8=

print('MyMagic8Ball에 오신것을 환영합니다')

#질문에 알맞은 답변 하는 일에 randint() 함수를 활용합니다.
choice=random.randint(1,8)
if choice==:1
    answer=ans1
elif choice==:2
    answer=ans2
elif choice==:3
    answer=ans3
elif choice==:4
    answer=ans4
elif choice==:5
    answer=ans5
elif choice==:6
    answer=ans6
elif choice==:7
    answer=ans7
else:
    answer=ans8
    
#사용자의 질문 얻기
question=input('조언을 구하고 싶으면 질문을 입력하고 엔터키를 누르세요.\n')

print('고민중..\n'*4)

#화면에 답변을 출력합니다.

print(answer)

input('\n\n 마치려면 엔터키를 누르세요')
