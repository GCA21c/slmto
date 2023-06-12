import random
from collections import Counter
from tqdm import tqdm
import colorama
from colorama import Fore, Style  # CMD상 COLOR 설정

colorama.init()  # 초기화

print(Fore.BLUE + Style.BRIGHT +
      f"V1.1 update : 생성된 각 세트는 중복숫자 허용")
input(Fore.GREEN + Style.BRIGHT + "살만이형의 행운을 담아 다섯 세트 생성 enter!\n")

# 45 이하의 숫자 행운숫자 x개 생성(x=행운숫자)
numbers = [random.randint(1, 45) for _ in tqdm(
    range(19850831), leave=True, bar_format='{l_bar}{bar:45}|')]  # barformat로 진행바 표시시 불필요한것들 삭제

print(Fore.BLUE + Style.BRIGHT +
      f"=====================================================")


# 가장 많이 생성된 숫자를 찾아서 리스트로 만들기
number_counts = Counter(numbers)
sorted_numbers = sorted(
    number_counts, key=lambda x: number_counts[x], reverse=True)
most_common_numbers = sorted_numbers[:30]  # 상위 30개 숫자 추출

# 상위 30개 숫자를 6개씩 자르기
number_sets = []
for i in range(5):
    number_set = random.sample(most_common_numbers, 6)  # 6개씩 랜덤으로 추출
    number_sets.append(number_set)

# 출력
for i, number_set in enumerate(number_sets):
    print(Fore.BLUE + Style.BRIGHT +
          f"\n 살만이형의 행운의 {i+1}번째 픽: {sorted(number_set)}\n" + Style.RESET_ALL)

print(Fore.BLUE + Style.BRIGHT +
      f"=====================================================" + Style.RESET_ALL)


input(Fore.RED + Style.BRIGHT + "\n살만이형의 기운을 담은 후 enter!" + Style.RESET_ALL)
