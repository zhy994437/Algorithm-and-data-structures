# Hash Table with Linear Probing

## Project Overview

This project implements a hash table data structure using linear probing for collision resolution. The hash table is designed specifically for storing lowercase English words, using a unique hash function that maps words based on their last character to one of 26 slots (corresponding to letters 'a' through 'z').

## Features

- **Hash Function**: Uses the last character of each word as the hash value
- **Collision Resolution**: Linear probing technique
- **Slot States**: Three possible states for each slot
  - "never used" - slot has never contained data
  - "tombstone" - slot previously contained data that was deleted
  - "occupied" - slot currently contains a key
- **Operations**:
  - Insert: Add words to the hash table
  - Delete: Remove words from the hash table (using tombstone marking)
  - Retrieval: Display all current keys in the table

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

The program accepts a single line of space-separated commands:

- **AWord**: Insert a word into the hash table (e.g., `Aapple` inserts "apple")
- **DWord**: Delete a word from the hash table (e.g., `Dapple` deletes "apple")

**Constraints:**
- Words must be lowercase English letters only
- Maximum word length: 10 characters
- Maximum number of operations: 26
- If a word already exists, insertion is ignored
- If a word doesn't exist, deletion is ignored

### Output Format

The program outputs all keys currently in the hash table, traversing slots from 'a' to 'z', separated by spaces.

## Examples

### Example 1: Basic Insertions

**Input:**
```
Aaaa Accc Abbb
```

**Output:**
```
aaa bbb ccc
```

**Explanation:** 
- `Aaaa`: Inserts "aaa" (hash value 'a', slot 0)
- `Accc`: Inserts "ccc" (hash value 'c', slot 2)
- `Abbb`: Inserts "bbb" (hash value 'b', slot 1)
- Output shows keys in slot order: a → b → c

---

### Example 2: Collision Handling

**Input:**
```
Abba Aaaa Acca
```

**Output:**
```
bba aaa cca
```

**Explanation:**
- `Abba`: Inserts "bba" (hash value 'a', slot 0)
- `Aaaa`: Tries slot 0 (occupied by "bba"), moves to slot 1 via linear probing
- `Acca`: Tries slot 0 (occupied), tries slot 1 (occupied), inserts at slot 2
- Output: bba (slot 0), aaa (slot 1), cca (slot 2)

---

### Example 3: Insertion and Deletion

**Input:**
```
Abba Aaaa Acca Daaa
```

**Output:**
```
bba cca
```

**Explanation:**
- After inserting "bba", "aaa", and "cca"
- `Daaa`: Deletes "aaa" (slot 1 becomes "tombstone")
- Output shows only remaining keys: bba and cca

---

### Example 4: Complex Operations

**Input:**
```
Adog Acat Afog Ddog Abat
```

**Output:**
```
cat fog bat
```

**Explanation:**
- "dog" and "fog" both hash to 'g', "cat" hashes to 't', "bat" hashes to 't'
- After deletion of "dog" and proper collision handling
- Output shows remaining keys in slot order

## How It Works

### Hash Function

The hash function extracts the last character of the word and converts it to a slot index:

```python
hash_value = ord(last_character) - ord('a')
```

For example:
- "apple" → last char 'e' → slot 4
- "banana" → last char 'a' → slot 0
- "cherry" → last char 'y' → slot 24

### Linear Probing

When a collision occurs (the target slot is already occupied), the algorithm:
1. Moves to the next slot: `(current_index + 1) % 26`
2. Continues until finding an available slot or confirming the key exists
3. Wraps around from slot 25 back to slot 0 if necessary

### Search Process

1. Calculate hash value from the last character
2. Check the corresponding slot:
   - If "never used" → key doesn't exist
   - If matches the key → found
   - If occupied by different key or "tombstone" → continue to next slot
3. Repeat until key is found or proven absent

### Insertion Process

1. Search to ensure the key doesn't already exist
2. If not found, calculate hash value
3. Find the first available slot ("never used" or "tombstone") using linear probing
4. Place the key in that slot

### Deletion Process

1. Search for the key using the search process
2. If found, mark the slot as "tombstone"
3. The tombstone allows future searches to continue probing past this slot

## Code Structure

### Class: HashTable

**Attributes:**
- `size`: Number of slots (26)
- `table`: Array storing slot states and keys

**Methods:**
- `hash(key)`: Computes hash value from last character
- `insert(key)`: Inserts a key using linear probing
- `delete(key)`: Deletes a key by marking slot as tombstone
- `getkey()`: Returns all currently stored keys

## Time Complexity

- **Average Case:**
  - Insert: O(1)
  - Delete: O(1)
  - Search: O(1)

- **Worst Case (all keys hash to same value):**
  - Insert: O(n)
  - Delete: O(n)
  - Search: O(n)

## Why Tombstones?

Tombstones are crucial for maintaining search correctness after deletions. Without tombstones, deleting a key would break the probe sequence for other keys that collided with it, making them unfindable.

## License

This project is provided as-is for educational purposes.
