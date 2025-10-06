package main

import (
	"fmt"
	"math"
)

func segitigaValid_103012300164(a, b, c float64) bool { //Luthfi Iriawan Fadhilah
	if a <= 0 || b <= 0 || c <= 0 {
		return false
	}
	max := maxSisi(a, b, c)
	sum := a + b + c - max
	return max < sum
}

