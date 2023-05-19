# matrix chain multiplication
import random
import time
import matplotlib.pyplot as plt

# Dynamic programming algorithm
def dynamic_programming(arr):
    n = len(arr)
    m = [[float("inf") for j in range(n)] for i in range(n)]
    s = [[0 for j in range(n)] for i in range(n)]

    # Initialize the diagonal elements of m.
    for i in range(1, n):
        m[i][i] = 0

    # Fill in the rest of m.
    for l in range(2, n):
        for i in range(1,n-l+1):
            j = i + l - 1
            for k in range(i, j):
                temp_cost = m[i][k] + m[k+1][j] + arr[i-1] * arr[k] * arr[j]
                if temp_cost < m[i][j]:
                    m[i][j] = temp_cost
                    s[i][j] = k
  # print the minimum cost and optimal parentheses.
    print('DP')
    print("Minimum cost : {}".format(m[1][-1]))
    print_optimal_parens(s, 1, len(arr)-1)
    print('')

temp = []

# Brute force algorithm
def brute_force(arr):
    n = len(arr)-1
    def recursive(i, j):
        if i == j:
            return 0
        minimum = float("inf")
        for k in range(i, j):
            cost = (recursive(i, k) + recursive(k+1, j) + arr[i-1] * arr[k] * arr[j])
                        
            if cost < minimum:
                minimum = cost
                temp.append(k)
                
        return minimum
    print('Brute Force')
    print("Minimum cost : {}".format(recursive(1, n)))
    print(temp)


    

#print the optimal parenthesization
def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")


def measure_execution_time(func, arr):

    start_time = time.process_time()
    func(arr)
    end_time = time.process_time()
    
    return round((end_time - start_time))
        

def main():
    step_size = 1
    max_size = 10
    algorithms = [dynamic_programming, brute_force]
    results = {algorithm.__name__: [] for algorithm in algorithms}
    for arr_size in range(3, max_size + step_size, step_size):
            arr = random.sample(range(1,arr_size+1), arr_size)
            print('-------------------')
            print(arr)
            print('iteartions:%d' %arr_size)
            for algorithm in algorithms:
                time = measure_execution_time(algorithm, arr)
                print(f"{algorithm.__name__} execution times: %d s" %time)
                results[algorithm.__name__].append(time)

                
    x = list(i for i in range(3, max_size + step_size, step_size))
    plt.plot(x, results['dynamic_programming'], 'ro--', linewidth=1, markersize=1,label = 'DP')
    plt.plot(x, results['brute_force'], 'go--', linewidth=1, markersize=1,label = 'Brute Force')
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()
