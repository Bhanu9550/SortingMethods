# Sorting Algorithms: Bubble Sort, Selection Sort, and Insertion Sort

***

## Bubble Sort

### Description
Bubble Sort is a simple comparison-based algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are out of order. This process continues until the list or array is sorted.

### Time Complexity

| Case         | Complexity | Explanation |
|---------------|-------------|-------------|
| Best Case     | O(n)        | When the array is already sorted. |
| Average Case  | O(n²)       | Standard number of swaps and comparisons. |
| Worst Case    | O(n²)       | When the array is in reverse order. |

### Space Complexity
- O(1) — Performs sorting in-place, requiring no extra memory.

***

## Selection Sort

### Description
Selection Sort divides the array into a sorted and an unsorted region. It repeatedly selects the smallest element from the unsorted region and moves it to the end of the sorted region.

### Time Complexity

| Case         | Complexity | Explanation |
|---------------|-------------|-------------|
| Best Case     | O(n²)       | Still needs to scan all elements. |
| Average Case  | O(n²)       | Comparison count doesn't change. |
| Worst Case    | O(n²)       | Always performs n² comparisons. |

### Space Complexity
- O(1) — In-place sorting algorithm.

***

## Insertion Sort

### Description
Insertion Sort works similarly to sorting playing cards in your hand. It takes one element from the unsorted part and inserts it into its correct position in the sorted part.

### Time Complexity

| Case         | Complexity | Explanation |
|---------------|-------------|-------------|
| Best Case     | O(n)        | Already sorted array, only one comparison per iteration. |
| Average Case  | O(n²)       | Roughly half of the elements need insertion. |
| Worst Case    | O(n²)       | Completely reversed array. |

### Space Complexity
- O(1) — Sorting is done within the array itself.

***

