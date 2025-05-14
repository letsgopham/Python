answers = ['a', 'b', 'd']

while True:
     
     answer = input("""요즘 내가 꽂힌 노래를 모두 고르시오.(정답을 입력할 때는 띄어서 입력해주세요.)
a) Smoking Dreams  b) 날씨의 요정  c) Pink + White  d) Disco Yes  e) peach eyes : """)
     print()
     
     selected = answer.split( )
     selected.sort()

     if answers == selected:
          print("정답.")
          break

     elif selected.count('e') >= 1:
          print("오답.")
          print()
          
     elif selected.count('c') >= 1:
          print("오답.")
          print()

     else:
          print("========모두 고르시오.========")
          print()
