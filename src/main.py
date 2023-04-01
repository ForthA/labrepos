from a_star import input_data_star
from greedy import input_data_greedy
from tests.greedy_test import greedy_test
from tests.a_star_test import a_star_test

if __name__ == "__main__":
    greedy_test()
    a_star_test()
    print("1 a_star, 2 greedy")
    choose = int(input())
    if choose == 1:
        input_data_star()
    else:
        input_data_greedy()
