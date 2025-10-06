# Road Network Reorganization

## Project Overview

This project solves a graph optimization problem: reorganizing a country's road network to ensure exactly one path exists between any pair of cities while minimizing the total cost of construction and destruction. The solution uses a Disjoint Set (Union-Find) data structure combined with a greedy algorithm similar to Kruskal's Minimum Spanning Tree algorithm.

## Problem Statement

Given a country with N cities:
- Some cities are currently connected by bidirectional roads
- Some city pairs have no connection (no path exists)
- Some city pairs have multiple different paths (redundant roads)

**Goal**: Rebuild the road network so that every pair of cities has exactly **one** path between them (creating a tree structure).

**Constraints**:
- Build new roads where needed
- Destroy existing redundant roads
- Minimize the total cost (building + destroying)

## Features

- **Disjoint Set (Union-Find)**: Efficient tracking of connected components
  - Path compression for optimized find operations
  - Union by rank for balanced tree structure
- **Cost Calculation**: Letter-based encoding (A-Z: 0-25, a-z: 26-51)
- **Greedy Algorithm**: Optimal edge selection for minimum cost
- **Graph Transformation**: Converts any graph to a spanning tree

## Requirements

- Python 3.x (no external dependencies required)

## How to Run

### Basic Execution

1. Save the code as `main.py`
2. Run the program from the command line:

```bash
python main.py
```

3. Enter your input when prompted

### Input Format

The program accepts **one line** with **three space-separated strings**:

```
country build destroy
```

Each string represents an N×N matrix in the format:
```
row1,row2,row3,...,rowN
```

Where each row contains N characters.

**Matrix Descriptions**:

1. **country[i][j]**: Current road network
   - `1` = road exists between city i and city j
   - `0` = no road exists

2. **build[i][j]**: Cost to build a road between cities i and j
   - `A-Z` = costs 0-25
   - `a-z` = costs 26-51

3. **destroy[i][j]**: Cost to destroy the road between cities i and j
   - Same encoding as build matrix

**Important Notes**:
- Matrices are symmetric (graph is undirected)
- Diagonal elements (i=i) are ignored
- All input must be on a single line

### Output Format

The program outputs a single integer: the minimum cost required to reorganize the road network.

## Examples

### Example 1: Disconnected Cities

**Input:**
```
000,000,000 ABD,BAC,DCA ABD,BAC,DCA
```

**Output:**
```
3
```

**Explanation:**
- 3 cities, completely disconnected
- Need to build 2 roads to connect all cities (creating a tree)
- Best strategy: Build 0-1 (cost 0) and 0-2 (cost 3)
- Total cost: 0 + 3 = 3

---

### Example 2: Triangle to Tree

**Input:**
```
011,101,110 ABD,BAC,DCA ABD,BAC,DCA
```

**Output:**
```
1
```

**Explanation:**
- 3 cities forming a complete triangle (3 roads)
- Need exactly 2 roads for 3 cities
- Must destroy 1 road
- Best strategy: Destroy road 0-1 (cost A = 0... wait, output is 1)
- Actually: Destroy road 1-0 (cost B = 1)
- Total cost: 1

---

### Example 3: Two Triangles

**Input:**
```
011000,101000,110000,000011,000101,000110 ABDFFF,BACFFF,DCAFFF,FFFABD,FFFBAC,FFFDCA ABDFFF,BACFFF,DCAFFF,FFFABD,FFFBAC,FFFDCA
```

**Output:**
```
7
```

**Explanation:**
- 6 cities forming two separate triangles (cities 0-1-2 and 3-4-5)
- Each triangle has 3 roads, needs only 2
- Must destroy 1 road per triangle (cost 1 each)
- Must connect the two components (cheapest is cost F = 5)
- Total cost: 1 + 1 + 5 = 7

---

### Example 4: Single City

**Input:**
```
0 A A
```

**Output:**
```
0
```

**Explanation:**
- Only 1 city, no roads needed
- Total cost: 0

---

### Example 5: Already Optimal

**Input:**
```
0001,0001,0001,1110 AfOj,fAcC,OcAP,jCPA AWFH,WAxU,FxAV,HUVA
```

**Output:**
```
0
```

**Explanation:**
- 4 cities already connected in a tree structure (3 roads)
- Cities 0, 1, 2 all connect to city 3
- Already has exactly one path between any two cities
- No reorganization needed
- Total cost: 0

## Algorithm Explanation

### Step-by-Step Process

1. **Parse Input**: Extract the three matrices (country, build, destroy)

2. **Create Edge Lists**:
   - **E1**: Existing roads with their destruction costs
   - **E2**: Non-existing roads with their construction costs

3. **Sort Edges**:
   - **E1**: Sort by cost (descending), then by indices
     - Prioritize keeping cheap-to-destroy roads (destroy expensive ones first)
   - **E2**: Sort by cost (ascending), then by indices
     - Prioritize building cheap roads

4. **Process Existing Roads (E1)**:
   - For each edge in E1 (highest destruction cost first):
     - If connecting different components → KEEP (merge components)
     - If connecting same component → DESTROY (add cost)

5. **Process Potential Roads (E2)**:
   - For each edge in E2 (lowest construction cost first):
     - If connecting different components → BUILD (add cost, merge components)
     - If connecting same component → SKIP (would create cycle)

### Why This Works

The algorithm builds a **Minimum Spanning Tree** with modified costs:
- Keeping an existing road has cost 0
- Destroying an existing road costs destroy[i][j]
- Building a new road costs build[i][j]

By processing existing roads first (keeping those that don't create cycles), we maximize road reuse and minimize destruction costs.

### Time Complexity

- Sorting edges: O(N² log N²) = O(N² log N)
- Union-Find operations: Nearly O(1) with path compression and union by rank
- Overall: **O(N² log N)**

## Code Structure

### Class: Disjointset

**Purpose**: Tracks connected components of cities

**Attributes**:
- `parent`: Parent pointer for each node
- `rank`: Rank for union by rank optimization

**Methods**:
- `find(x)`: Find root of component containing x (with path compression)
- `union(x, y)`: Merge components containing x and y

### Class: Reorganization

**Purpose**: Solves the road reorganization problem

**Methods**:
- `cost(ch)`: Convert letter to numeric cost (A-Z: 0-25, a-z: 26-51)
- `getcost(country, build, destroy)`: Calculate minimum reorganization cost

## Key Concepts

### Spanning Tree
A tree that connects all N cities using exactly N-1 roads. This ensures:
- Every city is reachable from every other city
- Exactly one path exists between any two cities
- No cycles exist in the network

### Disjoint Set (Union-Find)
An efficient data structure for:
- Tracking which cities are connected
- Merging connected components
- Detecting if adding a road would create a cycle

### Greedy Strategy
The algorithm makes locally optimal choices:
1. Keep existing roads that help connectivity (avoid destruction cost)
2. Destroy existing roads that create redundancy
3. Build new roads only when necessary for connectivity

## Edge Cases

- Single city: No roads needed (cost = 0)
- Already a tree: No reorganization needed (cost = 0)
- Complete graph: Must destroy many roads
- Disconnected graph: Must build connecting roads

## License

This project is provided as-is for educational purposes.
