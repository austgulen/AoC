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
	fmt.Println(len(reports))
	part1(reports)

}

func part1(reports [][]int) {
	sum := 0
	for _, report := range reports {
		if len(report) < 2 {
			sum++
			fmt.Println("<2", report)
			continue
		}
		if report[0] == report[1] {
			continue
		}
		if report[0] > report[1] {
			if assertDecreasing(report) {
				sum++
			}
			//mode = "decreasing"
		} else {
			if assertIncreasing(report) {
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

func absInt(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
