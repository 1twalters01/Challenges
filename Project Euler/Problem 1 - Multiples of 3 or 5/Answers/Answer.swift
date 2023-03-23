import Foundation

func multiples_of_3_and_5(limit: Int) -> Int {
    let new_limit = limit-1
    let (limit3, limit5, limit15)  = limits_for_3_5_and_15(limit: new_limit)
    let (summation3, summation5, summation15) = summations_for_3_5_and_15(limit3: limit3, limit5: limit5, limit15: limit15)
    let answer = summation3 + summation5 - summation15
    return Int(answer)
}

func limits_for_3_5_and_15(limit: Int) -> (Double, Double, Double) {
    let limit3: Double = Double(limit/3)
    let limit5: Double = Double(limit/5)
    let limit15: Double = Double(limit/15)
    return (limit3, limit5, limit15)
}

func summations_for_3_5_and_15(limit3: Double, limit5: Double, limit15: Double) -> (Double, Double, Double) {
    let summation3 = (pow(limit3, 2) + limit3)*3/2
    let summation5 = (pow(limit5, 2) + limit5)*5/2
    let summation15 = (pow(limit15, 2) + limit15)*15/2
    return (summation3, summation5, summation15)
}

print("Enter a number: ", terminator: "")
let value = Int(readLine()!)
print(multiples_of_3_and_5(limit: value!))