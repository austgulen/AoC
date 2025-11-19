package main

import (
	"aoc2024/utils"
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	input, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error while opening file.", err)
		return
	}

	var reports [][]int

	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		var levels []int
		for _, part := range parts {
			num, err := strconv.Atoi(part)
			if err != nil {
				fmt.Println("error converting %s: %w", part, err)
				return
			}
			levels = append(levels, num)
		}
		reports = append(reports, levels)
	}
	// fmt.Println(reports)
	//
	// fmt.Println(len(reports))
	part1(reports)
	part2(reports)

}

func part1(reports [][]int) {
	sum := 0
	for _, report := range reports {
		if assertIsSafe(report) {
			sum++
		}
		// if len(report) < 2 {
		// 	sum++
		// 	// fmt.Println("<2", report)
		// 	continue
		// }
		// if report[0] == report[1] {
		// 	continue
		// }
		// if report[0] > report[1] {
		// 	if assertDecreasing(report) {
		// 		sum++
		// 	}
		// 	//mode = "decreasing"
		// } else {
		// 	if assertIncreasing(report) {
		// 		sum++
		// 	}
		// }
	}
	fmt.Println("Sum of safe :", sum)

}

func part2(reports [][]int) {
	sum := 0
	for _, report := range reports {
		if assertIsSafe(report) {
			sum++
		} else {
			if semiSafe(report) {
				// fmt.Println("SEMISAFE", report)
				sum++
			}
		}
	}
	fmt.Println("Sum of safe :", sum)

}

func assertIncreasing(report []int) bool {
	for i := 1; i < len(report); i++ {
		diff := utils.AbsInt(report[i] - report[i-1])
		if report[i] <= report[i-1] || diff > 3 || diff < 1 {
			return false
		}
	}
	return true
}

func assertDecreasing(report []int) bool {
	for i := 1; i < len(report); i++ {
		diff := utils.AbsInt(report[i] - report[i-1])

		if report[i] >= report[i-1] || diff > 3 || diff < 1 {
			return false
		}
	}
	return true
}

func assertIsSafe(report []int) bool {
	if len(report) < 2 {
		return true
	}
	if report[0] > report[1] {
		return assertDecreasing(report)
	} else {
		return assertIncreasing(report)
	}

}

func semiSafe(report []int) bool {
	// check if safe with deletion
	// check first by removing first and last elem, then inner
	// fmt.Println(len(report))
	// if assertIsSafe(report[1:]) {
	// 	return true
	// }
	// if assertIsSafe(report[:len(report)-1]) {
	// 	return true
	// }
	for idx := 0; idx < len(report); idx++ {
		subList := append([]int{}, report[:idx]...)
		subList = append(subList, report[idx+1:]...)
		fmt.Println(report, idx, subList)
		if assertIsSafe(subList) {
			return true
		}
	}
	return false

}
