// utils/helpers.go
package utils

import (
	"bufio"
	"fmt"
	"os"
)

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

func ReadInput(path string) []byte {
	file, err := os.ReadFile(path)
	if err != nil {
		fmt.Println("Error reading input:", err)
		return nil
	}
	return file
}

// func OpenFile(path string)

// from

func ReadLineByLine(path string) []string {
	input, err := os.Open(path)
	if err != nil {
		fmt.Println("Error opening file", err)
	}
	defer input.Close() // from online, seems smart :^)

	var output []string

	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		output = append(output, scanner.Text())

	}

	return output
}

func ReadSections(path string) (rules []string, input []string, er error) {
	// "fun"-fact i learned: we can declare the return variables in the return signature
	// of the function! this is very neat, I think at least
	file, err := os.Open(path)
	if err != nil {
		return nil, nil, err
	}
	defer file.Close()
	// split reading into two sections:
	section := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			section++
			continue
		}
		if section == 0 {
			rules = append(rules, line)
		} else {
			input = append(input, line)
		}
	}
	return rules, input, nil

}
