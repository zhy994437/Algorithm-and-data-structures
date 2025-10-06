# AVL Tree Implementation

## Project Overview

This project implements a self-balancing AVL (Adelson-Velsky and Landis) tree with insertion, deletion, and three types of tree traversal operations. The AVL tree automatically maintains balance through rotations, ensuring O(log n) time complexity for search, insertion, and deletion operations.

## Features

- **AVL Tree Operations:**
  - Insert: Add values to the tree while maintaining AVL balance property
  - Delete: Remove values from the tree with automatic rebalancing
  - Automatic height balancing through left and right rotations

- **Tree Traversals:**
  - Preorder traversal (Root → Left → Right)
  - Inorder traversal (Left → Root → Right)
  - Postorder traversal (Left → Right → Root)

## Requirements

- Python 3.x (no external dependencies required)

## How to Run

### Basic Execution

1. Save the code as `avl_tree.py`
2. Run the program from the command line:

```bash
python avl_tree.py
```

3. Enter your input when prompted

### Input Format

The program accepts a single line of space-separated commands:

- **Aint**: Insert value `int` into the AVL tree (e.g., `A3` inserts 3)
- **Dint**: Delete value `int` from the AVL tree (e.g., `D5` deletes 5)
- **Traversal Command** (must be the last command):
  - `PRE`: Preorder traversal
  - `IN`: Inorder traversal
  - `POST`: Postorder traversal

**Notes:**
- Values must be between 1 and 100
- If a value already exists, insertion is ignored
- If a value doesn't exist, deletion is ignored
- If the tree is empty, the output will be "EMPTY"

## Examples

### Example 1: Inorder Traversal

**Input:**
```
A1 A2 A3 IN
```

**Output:**
```
1 2 3
```

**Explanation:** Inserts 1, 2, and 3, then performs inorder traversal (sorted order).

---

### Example 2: Preorder Traversal

**Input:**
```
A1 A2 A3 PRE
```

**Output:**
```
2 1 3
```

**Explanation:** After balancing, node 2 becomes the root, with 1 as left child and 3 as right child.

---

### Example 3: Empty Tree

**Input:**
```
A1 D1 POST
```

**Output:**
```
EMPTY
```

**Explanation:** Inserts 1, then deletes 1, resulting in an empty tree.

---

### Example 4: Complex Operations

**Input:**
```
A5 A3 A7 A2 A4 A6 A8 D3 IN
```

**Output:**
```
2 4 5 6 7 8
```

**Explanation:** Inserts multiple values, deletes 3, then displays in sorted order.

## Code Structure

### Classes

- **Node**: Represents a single node in the AVL tree
  - `key`: The value stored in the node
  - `left`: Pointer to left child
  - `right`: Pointer to right child
  - `height`: Height of the node for balance calculations

- **AVLTree**: Main AVL tree implementation
  - `insert(key)`: Public method to insert a value
  - `delete(key)`: Public method to delete a value
  - `preorder()`, `inorder()`, `postorder()`: Public traversal methods
  - Internal helper methods for balancing, rotating, and recursive operations

## Algorithm Details

### Balancing

The AVL tree maintains the balance property where the height difference between left and right subtrees of any node is at most 1. When this property is violated after insertion or deletion, the tree performs rotations:

- **Left Rotation**: Used when right subtree is too tall
- **Right Rotation**: Used when left subtree is too tall
- **Left-Right Rotation**: Combination for left-heavy nodes with right-heavy left child
- **Right-Left Rotation**: Combination for right-heavy nodes with left-heavy right child

### Time Complexity

- Insert: O(log n)
- Delete: O(log n)
- Traversal: O(n)

## License

This project is provided as-is for educational purposes.
