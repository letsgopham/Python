# 못 고르겠을 때 랜덤으로 골라주는 모듈

import random
from filter import rest


def random_choice():
    choice = input('랜덤으로 골라드릴까요?(예/아니오): ')
    if choice == "예":
        i = random.randrange(len())