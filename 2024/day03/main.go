package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
	input, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("error reading file:", err)
	}
	corruptedString := string(input)
	// https://regex101.com/r/IHxKB3/1
	part1(corruptedString)
	part2(corruptedString)

}

func part1(corruptedString string) {
	pattern := regexp.MustCompile(`mul\((\d{1,3}),\s*(\d{1,3})\)`)
	total := 0

	matches := pattern.FindAllStringSubmatch(corruptedString, -1)
	// fmt.Println(matches)
	for _, match := range matches {
		str1 := match[1]
		str2 := match[2]
		num1, err1 := strconv.Atoi(str1)
		num2, err2 := strconv.Atoi(str2)

		if err1 != nil || err2 != nil {
			fmt.Println("EError converting numbers for match %s", match[0])
		}
		total += num1 * num2
	}
	fmt.Println("Total: ", total)
}

func part2(corruptedString string) {
	// In the start, we are in do.
	flag := true
	pattern := regexp.MustCompile(`mul\((\d{1,3}),\s*(\d{1,3})\)|do\(\)|don't\(\)`)
	matches := pattern.FindAllStringSubmatch(corruptedString, -1)
	total := 0
	for _, match := range matches {
		// fmt.Println(match)
		if match[0] == "do()" {
			flag = true
		} else if match[0] == "don't()" {
			flag = false
		} else {
			if flag {
				num1, err1 := strconv.Atoi(match[1])
				num2, err2 := strconv.Atoi(match[2])
				if err1 != nil || err2 != nil {
					fmt.Println("Error parsing %s.", match[0])
				}
				total += num1 * num2
			}
		}
	}
	fmt.Println("Total: ", total)
}
