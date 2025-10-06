package main

import (
	"fmt"
	"math"
)

// 1️⃣ Fungsi untuk memeriksa apakah segitiga valid
func isValidTriangle(a, b, c float64) bool {
	if a <= 0 || b <= 0 || c <= 0 {
		return false
	}
	max := maxSide(a, b, c)
	sum := a + b + c - max
	return max < sum
}

// 2️⃣ Fungsi untuk membandingkan dua sisi dengan toleransi 1% (0.01)
func isEqual(x, y float64) bool {
	tolerance := 0.01 * math.Max(x, y)
	return math.Abs(x-y) <= tolerance
}

// 3️⃣ Fungsi untuk menentukan jenis segitiga
func classifyTriangle(a, b, c float64) string {
	if !isValidTriangle(a, b, c) {
		return "Tidak dapat membentuk segitiga."
	}

	if isEqual(a, b) && isEqual(b, c) {
		return "Segitiga Sama Sisi (Equilateral)"
	}

	// Cari sisi terbesar untuk cek segitiga siku-siku
	max := maxSide(a, b, c)
	var s1, s2 float64
	if max == a {
		s1, s2 = b, c
	} else if max == b {
		s1, s2 = a, c
	} else {
		s1, s2 = a, b
	}

	if isEqual(max*max, s1*s1+s2*s2) {
		return "Segitiga Siku-Siku (Right Triangle)"
	}

	if isEqual(a, b) || isEqual(b, c) || isEqual(a, c) {
		return "Segitiga Sama Kaki (Isosceles)"
	}

	return "Segitiga Bebas (Scalene)"
}

// 4️⃣ Fungsi untuk mencari sisi terbesar
func maxSide(a, b, c float64) float64 {
	if a >= b && a >= c {
		return a
	} else if b >= a && b >= c {
		return b
	}
	return c
}

// 5️⃣ Fungsi utama (main)
func main() {
	var a, b, c float64
	fmt.Println("=== Program Penentu Jenis Segitiga ===")
	fmt.Print("Masukkan sisi a: ")
	fmt.Scan(&a)
	fmt.Print("Masukkan sisi b: ")
	fmt.Scan(&b)
	fmt.Print("Masukkan sisi c: ")
	fmt.Scan(&c)

	result := classifyTriangle(a, b, c)
	fmt.Println("Hasil:", result)
}