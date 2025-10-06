# Base Arithmetic Operations

## Project Overview

This project implements fundamental arithmetic operations (addition, multiplication, and division) for integers in different number bases (base 2 to base 10). The implementation uses:

- **School Method** for integer addition
- **Karatsuba Algorithm** for integer multiplication
- **Custom Division** algorithm for integer division

## Features

- Supports bases from 2 (binary) to 10 (decimal)
- Handles large integers up to 100 digits
- Performs three operations in sequence:
  1. Addition using the school method
  2. Multiplication using Karatsuba algorithm
  3. Division with floor rounding (graduate students)
     - Undergraduate students can output 0 for division

## Requirements

- Python 3.x

## Installation

No additional packages are required. The project uses only Python standard library.

## How to Run

### Method 1: Using the Python Script

```bash
python main.py
```

### Method 2: Using Jupyter Notebook

```bash
jupyter notebook "python3 main.py.ipynb"
```

## Input Format

The program accepts a single line of input containing three space-separated values:

```
I1 I2 B
```

Where:
- `I1`: First non-negative integer (up to 100 digits)
- `I2`: Second non-negative integer (up to 100 digits)
- `B`: Base of the numbers (integer from 2 to 10)

## Output Format

The program outputs three space-separated results in the same base B:

```
sum product quotient
```

Where:
- `sum`: I1 + I2 (using school method)
- `product`: I1 × I2 (using Karatsuba algorithm)
- `quotient`: I1 ÷ I2 (floor division)

## Examples

### Example 1: Decimal (Base 10)
**Input:**
```
101 5 10
```
**Output:**
```
106 505 20
```

### Example 2: Binary (Base 2)
**Input:**
```
10 111 2
```
**Output:**
```
1001 1110 0
```

### Example 3: Binary (Base 2)
**Input:**
```
111 10 2
```
**Output:**
```
1001 1110 11
```

**Note for Undergraduates:** If you are an undergraduate student, output `0` for the division result instead of the actual quotient.

## Code Structure

### Main Functions

1. **`todecimal(num, base)`** / **`conversion(num, base)`**
   - Converts a number from any base to decimal

2. **`tobase(num, base)`**
   - Converts a decimal number to the specified base

3. **`schooladdition(I1, I2, base)`**
   - Implements school method addition
   - Converts inputs to decimal, adds them, then converts back

4. **`karatsubamultiplication(I1, I2, base)`**
   - Implements Karatsuba multiplication algorithm
   - Converts inputs to decimal, multiplies them, then converts back

5. **`customdivision(I1, I2, base)`**
   - Implements integer division
   - Converts inputs to decimal, performs floor division, then converts back

## Implementation Details

- All arithmetic operations are performed in decimal (base 10)
- Results are converted back to the original base for output
- Division uses integer floor division (`//` operator)
- I2 is guaranteed to be non-zero

## Testing

To test the program, you can run it with the provided examples:

```bash
echo "101 5 10" | python main.py
echo "10 111 2" | python main.py
echo "111 10 2" | python main.py
```

## Notes

- Ensure input numbers are valid for the specified base
- For base 2, only digits 0 and 1 are valid
- For base 10, digits 0-9 are valid
- The program assumes well-formed input

## License

This project is created for educational purposes as part of an algorithms course assignment.
