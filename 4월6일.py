while 트루나 1이나 같다!

---

<리스트>
중요! 인덱스는 0번부터 시작한다!
대괄호 -> 리스트다!
4p
ee = range(1, 11) -> 1부터 시작해서 10까지 하나씩 증가시켜줘~
찍었을 떄 우린 눈에는 그냥 range(1, 11)로 보임
다 볼려면 list()로 변환하기! ee = list(range(1,11))

8p
처음에 aa = [0, 0, 0, 0]이라고 써줘야지 오류가 나지 않는다.

슬라이싱
변수명[시작인덱스 : 마지막인덱스+1]

cards[:2] <-처음부터 cards[1]까지 슬라이싱

시험칠때 인덱스 번호 적어놓고 하면 더 안햇갈릴것!

alist[-2:-6] -> 순방향이니까 안된다! 그냥 [] 나옴

리스트 [ 첫번째값 : 두번째값 : 세번쨰값 ]
-> 첫번쨰값 안쓰면 첫째값, 두번째값안쓰면 끝값, 세번째값 안쓰면 1!

17p 섞여있을 때는 더해서 만들어주면 된다!
n[:3]+n[-1:-4:-1]
[4, 5, 6, 9, 8, 7]

18p aa.append(0) -> 빈리스트를 만들어서 0을 넣어줘~
