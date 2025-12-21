package main

import "fmt"

func main() {
	var my_array = []int{1, 2, 3, 10, 5}

	fmt.Println(my_array)
	fmt.Println(SortNumbers(my_array))

}

func SortNumbers(s []int) []int {
	if s == nil {
		return nil
	}

	for i := 0; i < len(s); i++ {
		for j := i; j < len(s); j++ {
			if is_greater(&s[i], &s[j]) {
				swap(&s[i], &s[j])
			}
		}
	}
	return s
}

func is_greater(a *int, b *int) bool {
	if *a > *b {
		return true
	} else {
		return false
	}
}

func swap(p *int, t *int) (int, int) {
	var temp int

	temp = *p
	*p = *t
	*t = temp

	return *p, *t
}
