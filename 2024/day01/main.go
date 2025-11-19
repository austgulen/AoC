package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	input, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error while opening file.", err)
		return
	}
	var L []int
	var R []int
	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		valL, errL := strconv.Atoi(parts[0])
		valR, errR := strconv.Atoi(parts[1])

		if errL != nil || errR != nil {
			fmt.Println("Error in converting", line)
			continue
		}
		L = append(L, valL)
		R = append(R, valR)

	}
	//fmt.Println("L sorted", L)
	part1(L, R)
	part2(L, R)

}

func part1(L []int, R []int) {
	// Get the distance between the two sorted lists
	sort.Ints(L)
	sort.Ints(R)

	distance := 0
	for i := range L {
		diff := int(math.Abs(float64(L[i] - R[i])))
		distance += diff
	}
	fmt.Println("DISTANCE = ", distance)
}

func part2(L []int, R []int) {
	// Get the simmilarity score of the two lists:
	simScore := 0
	freq := make(map[int]int)
	for _, num := range R {
		freq[num]++
	}
	// fmt.Println(freq)
	for _, num := range L {
		simScore += num * freq[num]
	}
	fmt.Println("simScore", simScore)
}
