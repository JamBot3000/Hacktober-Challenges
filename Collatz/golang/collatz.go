package main

import (
	"fmt"
	"os"
	"strconv"
)

func usage() { fmt.Println("Usage: ./collatz <positive int>") }

func main() {
	if len(os.Args) < 2 {
		usage()
		return
	}
	num, err := strconv.Atoi(os.Args[1])
	if err != nil || num < 1 {
		usage()
		return
	}

	fmt.Print(num, " ")
	for num > 1 {
		if num%2 == 0 {
			num /= 2
		} else {
			num *= 3
			num++
		}
		fmt.Print(num, " ")
	}
	if num < 0 {
		fmt.Println("Overflowed.")
	}
}
