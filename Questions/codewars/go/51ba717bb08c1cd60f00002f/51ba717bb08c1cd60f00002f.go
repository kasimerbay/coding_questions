package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var my_array []int = []int{-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20}

	fmt.Println(sub_range(my_array))
}

func sub_range(list []int) string {

	var result []string
	n := len(list)

	for i := 0; i < n; i++ {
		startIdx := i
		// Expand the range as far as possible
		for i+1 < n && list[i+1] == list[i]+1 {
			i++
		}
		endIdx := i

		// Rule: It is not a range unless it spans at least 3 numbers
		if endIdx-startIdx >= 2 {
			result = append(result, fmt.Sprintf("%d-%d", list[startIdx], list[endIdx]))
		} else {
			// If it's only 1 or 2 numbers, add them individually
			for j := startIdx; j <= endIdx; j++ {
				result = append(result, strconv.Itoa(list[j]))
			}
		}
	}
	return strings.Join(result, ",")
}
