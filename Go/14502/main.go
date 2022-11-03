package main

import (
	"fmt"
)

var dx = [4]int{-1, 0, 1, 0}
var dy = [4]int{0, -1, 0, 1}
var n int
var m int
var ans int = 0

var arr [][]int

type point struct {
	y int
	x int
}

func main() {
	fmt.Scan(&n)
	fmt.Scan(&m)
	arr = make([][]int, n)

	for i := 0; i < n; i++ {
		arr[i] = make([]int, m)
		for j := 0; j < m; j++ {
			fmt.Scan(&arr[i][j])
		}
	}
	wall(0)
	defer println(ans)
}

func wall(cnt int) {
	if cnt == 3 {
		virus()
		return
	}
	for i := range arr {
		for j := range arr[i] {
			if arr[i][j] == 0 {
				arr[i][j] = 1
				wall(cnt + 1)
				arr[i][j] = 0
			}
		}
	}
}

func virus() {
	var qu []point
	labArr := make([][]int, n)
	for i := range labArr {
		labArr[i] = make([]int, m)
		copy(labArr[i], arr[i])
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if labArr[i][j] == 2 {
				qu = append(qu, point{y: i, x: j})
			}
		}
	}

	for len(qu) != 0 {
		p := qu[0]
		qu = qu[1:]

		for i := 0; i < 4; i++ {
			nx := p.x + dx[i]
			ny := p.y + dy[i]

			if nx < 0 || nx >= m || ny < 0 || ny >= n {
				continue
			}
			if labArr[ny][nx] == 0 {
				labArr[ny][nx] = 2
				qu = append(qu, point{y: ny, x: nx})
			}
		}
	}
	zeroCount := 0
	for i := range labArr {
		for j := range labArr[i] {
			if labArr[i][j] == 0 {
				zeroCount++
			}
		}
	}
	if zeroCount > ans {
		ans = zeroCount
	}
}
