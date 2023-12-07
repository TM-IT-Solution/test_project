package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) != 4 {
		fmt.Println("Usage: calculator <number> <operator> <number>")
		os.Exit(1)
	}

	// Parse command line arguments
	num1, err := strconv.ParseFloat(os.Args[1], 64)
	if err != nil {
		fmt.Println("Error parsing number 1:", err)
		os.Exit(1)
	}

	operator := os.Args[2]

	num2, err := strconv.ParseFloat(os.Args[3], 64)
	if err != nil {
		fmt.Println("Error parsing number 2:", err)
		os.Exit(1)
	}

	// Perform calculation based on the operator
	var result float64

	switch operator {
	case "+":
		result = num1 + num2
	case "-":
		result = num1 - num2
	case "*":
		result = num1 * num2
	case "/":
		if num2 == 0 {
			fmt.Println("Error: Division by zero")
			os.Exit(1)
		}
		result = num1 / num2
	default:
		fmt.Println("Invalid operator:", operator)
		os.Exit(1)
	}

	// Print the result
	fmt.Printf("Result: %v %s %v = %v\n", num1, operator, num2, result)
}
