## Travel Itinerary Optimization Problem:

### Problem Statement:
You are tasked with optimizing the travel itinerary for a delivery service that needs to visit multiple cities. The company has a list of cities to visit, and the cost associated with traveling between each pair of cities. Your objective is to determine the minimum travel cost required to visit each city exactly once and return to the starting city. This optimization is crucial for minimizing fuel costs and delivery times.

Given the number of cities and a matrix representing the travel costs between each pair of cities, develop an algorithm to calculate the minimum possible travel cost.

### Input:
- `n`: An integer representing the number of cities.
- `travel_matrix`: A 2D list of integers where `travel_matrix[i][j]` represents the travel cost from city `i` to city `j`. The matrix is symmetric (`travel_matrix[i][j] = travel_matrix[j][i]`) and the diagonal elements are zero (`travel_matrix[i][i] = 0`).

### Output:
- An integer representing the minimum travel cost required to visit all cities exactly once and return to the starting city.

### Constraints:
- `1 <= n <= 20`: The number of cities is small enough to allow for a dynamic programming approach.
- The matrix will have non-negative integers, and the cost of traveling from a city to itself is 0.

### Example:

Given cities `A`, `B`, `C`, and `D`, the `travel_matrix` is as follows:

|   | A  | B  | C  | D  |
|---|----|----|----|----|
| A |  0 |  5 | 10 | 20 |
| B |  5 |  0 | 11 |  6 |
| C | 10 | 11 |  0 | 18 |
| D | 20 |  6 | 18 |  0 |

**Example Input:**
n = 4
travel_matrix = [
    [0,   5, 10, 20]  # A
    [5,   0, 11,  6]  # B
    [10, 11,  0, 18]  # C
    [20,  6, 18,  0]  # D
]

**Example Output:**
34
The optimal route is A -> B -> D -> C -> A
5 (A->B) + 6 (B->D) + 18 (D->C) + 10 (C->A) = 39