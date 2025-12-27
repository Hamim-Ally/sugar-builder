// calculator.cpp - Calculator Implementation

#include "calculator.h"

Calculator::Calculator() : operation_count(0) {
}

int Calculator::add(int a, int b) {
    operation_count++;
    return a + b;
}

int Calculator::subtract(int a, int b) {
    operation_count++;
    return a - b;
}

int Calculator::multiply(int a, int b) {
    operation_count++;
    return a * b;
}

double Calculator::divide(int a, int b) {
    operation_count++;
    if (b == 0) {
        return 0.0;  // Error handling: division by zero
    }
    return static_cast<double>(a) / b;
}
