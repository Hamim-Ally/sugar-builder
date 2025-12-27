// main.cpp - Calculator Example Program

#include <iostream>
#include "calculator.h"

int main() {
    std::cout << "================================" << std::endl;
    std::cout << "  Calculator Example Program" << std::endl;
    std::cout << "================================" << std::endl;
    std::cout << std::endl;
    
    // Create a calculator instance
    Calculator calc;
    
    // Test addition
    int result1 = calc.add(10, 5);
    std::cout << "10 + 5 = " << result1 << std::endl;
    
    // Test subtraction
    int result2 = calc.subtract(10, 5);
    std::cout << "10 - 5 = " << result2 << std::endl;
    
    // Test multiplication
    int result3 = calc.multiply(10, 5);
    std::cout << "10 * 5 = " << result3 << std::endl;
    
    // Test division
    double result4 = calc.divide(10, 5);
    std::cout << "10 / 5 = " << result4 << std::endl;
    
    std::cout << std::endl;
    std::cout << "================================" << std::endl;
    std::cout << "Program completed successfully!" << std::endl;
    std::cout << "================================" << std::endl;
    
    return 0;
}
