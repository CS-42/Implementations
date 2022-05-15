package main

import (
	"fmt"
	"strconv"
)

func main() {

	inputInvalid := true
	var input string
	for inputInvalid {
		input = getInput()

		inputInvalid = !validateInput(input)

		if inputInvalid {
			fmt.Println("Invalid input. Please try again.")
		}
	}

	sum := everyOtherAddition(input)

	for len(strconv.Itoa(sum)) > 1 {
		sum = sumDigits(strconv.Itoa(sum))
	}

	fmt.Print("Output: ", sum)

}

// GetInput prompts the user for input and returns the input
func getInput() string {
	var input string
	fmt.Print("Input: ")
	fmt.Scanln(&input)
	return input
}

// ValidateInput takes a string and validates that the string is a valid number, it is positive, and is <= 10 digits
func validateInput(input string) bool {

	if len(input) > 10 {
		return false
	}

	inputInt, err := strconv.Atoi(input)
	if err != nil {
		return false
	}

	if inputInt < 0 {
		return false
	}

	return true
}

// EveryOtherAddition takes a string and returns the sum of every other digit
func everyOtherAddition(input string) int {
	strArr := []rune(input)
	var sum int
	for i := 1; i < len(strArr); i += 2 {
		digit, _ := strconv.Atoi(string(strArr[i]))
		sum += digit
	}
	return sum
}

// SumDigits takes a string and returns the sum of the digits
func sumDigits(input string) int {
	strArr := []rune(input)
	var sum int
	for i := 0; i < len(strArr); i += 1 {
		digit, _ := strconv.Atoi(string(strArr[i]))
		sum += digit
	}
	return sum
}
