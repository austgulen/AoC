package main

import (
	"aoc2024/utils"
	"fmt"
	"regexp"
	"strconv"
	"strings"
	// "regexp"
)

func main() {
	rules, input, err := utils.ReadSections("input.txt")
	if err != nil {
		panic(err)
	}
	// fmt.Println(rules)
	part1(rules, input)

}

func part1(rules []string, input []string) {
	// let us do some regular expressions! :D
	sum := 0
	reg, err := parseRules(rules)
	if err != nil {
		panic(err)
	}
	// fmt.Println(reg)
	for _, line := range input {
		if !reg.MatchString(line) {
			parts := strings.Split(line, ",")
			middle := parts[len(parts)/2]
			fmt.Println(line, middle)
			num, err := strconv.Atoi(middle)
			fmt.Println(num)
			if err != nil {
				panic(err)
			}
			sum += num
		}
	}
	fmt.Println("SUM PART 1 :", sum)
}

func part2(rules []string, input []string) {
	// let us do some regular expressions! :D
	sum := 0
	reg, err := parseRules(rules)
	if err != nil {
		panic(err)
	}
	// fmt.Println(reg)
	for _, line := range input {
		if !reg.MatchString(line) {
			parts := strings.Split(line, ",")
			middle := parts[len(parts)/2]
			fmt.Println(line, middle)
			num, err := strconv.Atoi(middle)
			fmt.Println(num)
			if err != nil {
				panic(err)
			}
			sum += num
		}
	}
	fmt.Println("SUM PART 1 :", sum)
}

// return the pointer since the struct may be large? a bit confused still but seems good
func parseRules(rules []string) (*regexp.Regexp, error) {
	var patterns []string
	for _, rule := range rules {
		parts := strings.Split(rule, "|")
		X, Y := parts[0], parts[1]
		patterns = append(patterns, "("+Y+".+"+X+")")
	}
	megaRule := strings.Join(patterns, "|")
	return regexp.Compile(megaRule)
}
