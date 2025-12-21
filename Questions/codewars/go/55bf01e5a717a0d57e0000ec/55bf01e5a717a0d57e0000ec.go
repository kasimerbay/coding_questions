package main

import "fmt"

func main() {
	var num int = 25

	fmt.Println(Persistence(num))
}

func multiply_digits(num int) int {
	var result int = 1

	for num > 0 {

		result *= num % 10

		num = num / 10
	}

	return result
}

func Persistence(n int) int {
	var result int = 0

	for n >= 10 {

		result += 1

		n = multiply_digits(n)
	}

	return result
}
