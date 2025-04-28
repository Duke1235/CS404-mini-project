import time
import random
import matplotlib.pyplot as plt

# ---------------------
# Search Algorithms
# ---------------------
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ---------------------
# Sorting Algorithms
# ---------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if len(arr) == 0:
        return arr
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

# ---------------------
# Plot Functions
# ---------------------

def plot_search_algorithms(input_sizes, linear_times, binary_times):
  plt.figure()
  plt.plot(input_sizes, linear_times, label='Linear Search', marker='o')
  plt.plot(input_sizes, binary_times, label='Binary Search', marker='s')
  plt.xlabel('Input Size')
  plt.ylabel('Execution Time (seconds)')
  plt.title('Search Algorithm Performance')
  plt.legend()
  plt.grid(True)
  plt.tight_layout()
  plt.show()

def plot_sort_algorithms(input_sizes, insertion_times, merge_times, radix_times):
  plt.figure()
  plt.plot(input_sizes, insertion_times, label='Insertion Sort', marker='o')
  plt.plot(input_sizes, merge_times, label='Merge Sort', marker='s')
  plt.plot(input_sizes, radix_times, label='Radix Sort', marker='^')
  plt.xlabel('Input Size')
  plt.ylabel('Execution Time (seconds)')
  plt.title('Sorting Algorithm Performance')
  plt.legend()
  plt.grid(True)
  plt.tight_layout()
  plt.show()

def plot_combined_algorithms(input_sizes, linear_times, binary_times, insertion_times, merge_times, radix_times):
  plt.figure()
  plt.plot(input_sizes, linear_times, label='Linear Search', marker='o')
  plt.plot(input_sizes, binary_times, label='Binary Search', marker='s')
  plt.plot(input_sizes, insertion_times, label='Insertion Sort', marker='^')
  plt.plot(input_sizes, merge_times, label='Merge Sort', marker='d')
  plt.plot(input_sizes, radix_times, label='Radix Sort', marker='x')
  plt.xlabel('Input Size')
  plt.ylabel('Execution Time (seconds)')
  plt.title('Search and Sort Algorithm Performance (Log Scale)')
  plt.yscale('log')
  plt.legend()
  plt.grid(True, which="both", ls="--")
  plt.tight_layout()
  plt.show()
# ---------------------
# Menu
# ---------------------
def display_menu():
  print("\nChoose which graph to display:")
  print("1. Search Algorithms Performance")
  print("2. Sorting Algorithms Performance")
  print("3. Combined Search and Sort (Log Scale)")
  print("4. Exit")
# ---------------------
# Benchmark
# ---------------------
input_sizes = [10, 100, 1000, 5000, 10000, 20000]

# Timing lists
linear_times = []
binary_times = []

insertion_times = []
merge_times = []
radix_times = []

print("Analyzing search and sort algorithm performance...\n")
print(f"{'Input Size':>10} | {'Linear (s)':>12} | {'Binary (s)':>12} | {'Insertion (s)':>15} | {'Merge (s)':>12} | {'Radix (s)':>12}")
print("-" * 75)

for size in input_sizes:
    test_data = list(range(size))  # Sorted data for searches
    random_data = [random.randint(0, size) for _ in range(size)]  # Random data for sorting

    target = size - 1  # Worst case for linear search

    # Linear Search
    start_time = time.perf_counter()
    linear_search(test_data, target)
    linear_time = time.perf_counter() - start_time
    linear_times.append(linear_time)

    # Binary Search
    start_time = time.perf_counter()
    binary_search(test_data, target)
    binary_time = time.perf_counter() - start_time
    binary_times.append(binary_time)

    # Insertion Sort
    insertion_data = random_data.copy()
    start_time = time.perf_counter()
    insertion_sort(insertion_data)
    insertion_time = time.perf_counter() - start_time
    insertion_times.append(insertion_time)

    # Merge Sort
    merge_data = random_data.copy()
    start_time = time.perf_counter()
    merge_sort(merge_data)
    merge_time = time.perf_counter() - start_time
    merge_times.append(merge_time)

    # Radix Sort
    radix_data = random_data.copy()
    start_time = time.perf_counter()
    radix_sort(radix_data)
    radix_time = time.perf_counter() - start_time
    radix_times.append(radix_time)

    print(f"{size:>10} | {linear_time:>12.8f} | {binary_time:>12.8f} | {insertion_time:>15.8f} | {merge_time:>12.8f} | {radix_time:>12.8f}")



# ---------------------
# Complexity Analysis
# ---------------------
print("\nTime Complexity Discussion:")
print("- Linear Search: O(n)")
print("- Binary Search: O(log n)")
print("- Insertion Sort: O(n^2) worst case, O(n) best case")
print("- Merge Sort: O(n log n) in all cases")
print("- Radix Sort: O(nk), where k is number of digits")

print("\nSpace Complexity Discussion:")
print("- Linear Search: O(1)")
print("- Binary Search: O(1)")
print("- Insertion Sort: O(1)")
print("- Merge Sort: O(n) (needs temporary arrays)")
print("- Radix Sort: O(n + k) (needs counting/output arrays)")

# ---------------------
# Menu
# ---------------------

while True:
  display_menu()
  choice = input("Enter your choice (1-4): ")

  if choice == '1':
      plot_search_algorithms(input_sizes, linear_times, binary_times)
  elif choice == '2':
      plot_sort_algorithms(input_sizes, insertion_times, merge_times, radix_times)
  elif choice == '3':
      plot_combined_algorithms(input_sizes, linear_times, binary_times, insertion_times, merge_times, radix_times)
  elif choice == '4':
      print("Exiting program.")
      break
  else:
      print("Invalid choice. Please select a valid option.")