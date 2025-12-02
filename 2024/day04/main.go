// idea:
// can we seach for all x's, and check if xmas is
// either on the diag, normal, backwards, or vertical?
// BYTE TO CHR: (decimal)
//
// X = 88
// M = 77
// A = 65
// S = 83
// NOTE: there is probably a smart way to do this, but this seems to do the trick :^)
package main

import (
	"aoc2024/utils"
	"fmt"
)

func main() {
	input := utils.ReadLineByLine("input.txt")
	// fmt.Println(input)
	part1(input)
	part2(input)
}

func part1(input []string) {
	sum := 0
	// iterate over rows
	for row := 0; row < len(input); row++ {
		//iterate over chars in row (cols)
		// fmt.Println(input[row])
		for col, char := range input[row] {
			if char == 'X' {
				// fmt.Println("found x")
				sum += checkValid(input, row, col)
			}
		}
	}
	fmt.Println("TOTAL NUMBER OF XMAS: ", sum)
}

func part2(input []string) {
	sum := 0
	for row := 1; row < len(input)-1; row++ {
		for col := 1; col < len(input[row])-1; col++ {
			if input[row][col] == 'A' {
				sum += checkValid2(input, row, col)
			}
		}
	}
	fmt.Println("TOTAL NUMBER OF X-MAS: ", sum)
}

func checkValid(input []string, rowIdx int, colIdx int) int {
	// check diag, horizintal, and vertical, in both directions
	// NOTE: there can be multiple occurances rooted in the same 'X'
	//
	/* HORIZONTAL */
	// forward
	sum := 0
	if colIdx <= len(input[rowIdx])-4 {
		if input[rowIdx][colIdx+1] == 'M' && input[rowIdx][colIdx+2] == 'A' && input[rowIdx][colIdx+3] == 'S' {
			sum++
		}
	}
	// backwards
	if colIdx >= 3 {
		if input[rowIdx][colIdx-1] == 'M' && input[rowIdx][colIdx-2] == 'A' && input[rowIdx][colIdx-3] == 'S' {
			sum++
		}
	}

	/* VERTICAL */
	// downwards
	if rowIdx <= len(input)-4 {
		if input[rowIdx+1][colIdx] == 'M' && input[rowIdx+2][colIdx] == 'A' && input[rowIdx+3][colIdx] == 'S' {
			sum++
		}
	}
	// upwards
	if rowIdx >= 3 {
		if input[rowIdx-1][colIdx] == 'M' && input[rowIdx-2][colIdx] == 'A' && input[rowIdx-3][colIdx] == 'S' {
			sum++
		}
	}
	/*DIAGONAL*/
	// down right
	if rowIdx <= len(input)-4 && colIdx <= len(input[rowIdx])-4 {
		if input[rowIdx+1][colIdx+1] == 'M' && input[rowIdx+2][colIdx+2] == 'A' && input[rowIdx+3][colIdx+3] == 'S' {
			sum++
		}
	}
	// down left
	if rowIdx <= len(input)-4 && colIdx >= 3 {
		if input[rowIdx+1][colIdx-1] == 'M' && input[rowIdx+2][colIdx-2] == 'A' && input[rowIdx+3][colIdx-3] == 'S' {
			sum++
		}
	}
	// up left
	if rowIdx >= 3 && colIdx <= len(input[rowIdx])-4 {
		if input[rowIdx-1][colIdx+1] == 'M' && input[rowIdx-2][colIdx+2] == 'A' && input[rowIdx-3][colIdx+3] == 'S' {
			sum++
		}
	}

	// up right
	if rowIdx >= 3 && colIdx >= 3 {
		if input[rowIdx-1][colIdx-1] == 'M' && input[rowIdx-2][colIdx-2] == 'A' && input[rowIdx-3][colIdx-3] == 'S' {
			sum++
		}
	}

	return sum
}

func checkValid2(input []string, row int, col int) int {
	word1 := string(input[row-1][col-1]) + string(input[row+1][col+1])
	word2 := string(input[row-1][col+1]) + string(input[row+1][col-1])
	// fmt.Println(word1, word2)
	valid1 := word1 == "MS" || word1 == "SM"
	valid2 := word2 == "MS" || word2 == "SM"
	if valid1 && valid2 {
		return 1
	}
	return 0
}
