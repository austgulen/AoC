// utils/helpers.go
package utils

import "fmt"

// "fmt"
func test() {
	fmt.Println("TEST")
}

func AbsInt(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
