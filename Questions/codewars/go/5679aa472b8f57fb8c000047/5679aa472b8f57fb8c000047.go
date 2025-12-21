package main

import "fmt"

func main() {
	var my_array = []int{20, 10, -80, 10, 10, 15, 35}

	fmt.Println(FindEvenIndex(my_array))
}

func FindEvenIndex(arr []int) int {
	var left_hand_slice []int
	var right_hand_slice []int

	for key, _ := range arr {
		left_hand_slice, right_hand_slice = slice_slicer(key, &arr)

		if sum(&left_hand_slice) == sum(&right_hand_slice) {
			return key
		}
	}

	return -1
}

func slice_slicer(index int, arr *[]int) ([]int, []int) {
	var left_hand_slice []int
	var right_hand_slice []int

	for key, value := range *arr {
		if key < index {
			left_hand_slice = append(left_hand_slice, value)
		} else if key > index {
			right_hand_slice = append(right_hand_slice, value)
		}
	}

	return left_hand_slice, right_hand_slice
}

func sum(s *[]int) int {
	sum := 0

	for _, i := range *s {
		sum += i
	}

	return sum
}
