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

func equal_103012300351(x, y float64) bool { // Jiyad Arsal Asari
	syarat:= 0.01 * math.Max(x, y)
	return math.Abs(x-y) <= syarat
}

func KlasifikasiSegitiga_103012300521(a, b, c float64) string {// Mahardika Naufal
	if !segitigaValid_103012300164(a, b, c) {
		return "Tidak dapat membentuk segitiga."
	}

	if equal_103012300351(a, b) && equal_103012300351(b, c) {
		return "Segitiga Sama Sisi (Equilateral)"
	}

	max := maxSisi(a, b, c)
	var s1, s2 float64
	if max == a {
		s1, s2 = b, c
	} else if max == b {
		s1, s2 = a, c
	} else {
		s1, s2 = a, b
	}

	if equal_103012300351(max*max, s1*s1+s2*s2) {
		return "Segitiga Siku-Siku (Right Triangle)"
	}

	if equal_103012300351(a, b) || equal_103012300351(b, c) || equal_103012300351(a, c) {
		return "Segitiga Sama Kaki (Isosceles)"
	}

	return "Segitiga Bebas (Scalene)"
}

func sisiMax_103012300008(a, b, c float64) float64{// Achmad Azhar Faiz Sabiq
	if a >= b && a >= c {
		return a
	} else if b >= a && b >= c {
		return b
	}
	return c
}
