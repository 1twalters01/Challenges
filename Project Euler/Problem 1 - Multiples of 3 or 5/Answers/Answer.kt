import kotlin.math.pow

fun main() {
    print("Enter a number: ")
    val value: Int = readLine()!!.toInt()
    var res: Int = multiples_of_3_and_5(value)
    println(res)
}

fun multiples_of_3_and_5(limit: Int): Int {
    var new_limit: Int = limit-1
    var (limit3: Double, limit5: Double, limit15: Double) = limits_for_3_5_and_15(new_limit)
    var (summation3: Int, summation5: Int, summation15: Int) = summations_for_3_5_and_15(limit3, limit5, limit15)
    var answer: Int = summation3 + summation5 - summation15
    return (answer)
}

fun limits_for_3_5_and_15(limit: Int): Triple<Double, Double, Double> {
    // Make these doubles as the power operator only works with doubles or floats
    var limit3: Double = limit / 3.0
    var limit5: Double = limit / 5.0
    var limit15: Double  = limit / 15.0
    return Triple(limit3, limit5, limit15)
}

fun summations_for_3_5_and_15(limit3: Double, limit5: Double, limit15: Double): Triple<Int, Int, Int> {
    var summation3: Int = (limit3.pow(2) + limit3).toInt()*3/2
    var summation5: Int = (limit5.pow(2) + limit5).toInt()*5/2
    var summation15: Int = (limit15.pow(2) + limit15).toInt()*15/2
    return Triple(summation3, summation5, summation15)
}