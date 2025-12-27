// calculator.h - Simple Calculator Class

#ifndef CALCULATOR_H
#define CALCULATOR_H

class Calculator {
public:
    Calculator();
    
    // Basic arithmetic operations
    int add(int a, int b);
    int subtract(int a, int b);
    int multiply(int a, int b);
    double divide(int a, int b);
    
private:
    int operation_count;
};

#endif // CALCULATOR_H
