# Python Calculator with Arithmetic and Trigonometric Functions

This Python program implements a calculator with various functionalities:

1. Basic arithmetic operations: Addition, Subtraction, Multiplication, Division
2. Additional operations: Square root, Square of a number
3. Trigonometric functions: Sine, Cosine, Tangent, Inverse Sine, Inverse Cosine, Inverse Tangent

## Getting Started

### Prerequisites

- Python 3.x (Recommended)

### Running the Program

1. Clone the repository or download the `calculator.py` file.
   
2. Open a terminal or command prompt.

3. Navigate to the directory where `calculator.py` is located.

4. Run the following command to execute the program:
   ```
   python calculator.py
   ```

5. Follow the on-screen instructions to perform calculations.

## Usage

- Upon running the program, you will see a menu with options to choose from.
- Enter your choice (1/2/3/4/5/6/7/8/9/10/11/12) based on the operation you want to perform:
  - **Basic Arithmetic Operations**:
    - Enter two numbers when prompted for addition, subtraction, multiplication, or division.
  - **Additional Operations**:
    - For square root and square operations, enter one number when prompted.
  - **Trigonometric Functions**:
    - For sine, cosine, tangent, arcsine, arccosine, and arctangent operations, enter the number (in radians) or a value between -1 to 1 for arcsine and arccosine.
  
- The program will display the result of the chosen operation.

## Notes

- Division by zero is handled gracefully, showing an error message instead of crashing.
- The square root function handles negative numbers by indicating that the square root is not real.
- For inverse trigonometric functions (`asin`, `acos`), ensure the input value falls within the valid range (`-1` to `1`) to avoid errors.
- Ensure to input valid numbers as per the operation you choose to avoid unexpected results.

---

Feel free to modify and expand this README further based on specific use cases or additional features you might add to the calculator program.
