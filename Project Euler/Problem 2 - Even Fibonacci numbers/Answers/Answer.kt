fun main() {
    print("Enter a number: ")
    val input: Int = readLine()!!.toInt()
    val res: Iterator<Int> = fib(input)
    var summation: Int = 0
    for (value in res) {
        if (value % 2 == 0) {
            summation += value
        }
    }
    println(summation)
}

fun fib(limit: Int) = iterator {
    var (a: Int, b: Int) = Pair(1, 2)
    while (a < limit) {
        a = b.also { b = a+b }
        yield (a)
    }
}