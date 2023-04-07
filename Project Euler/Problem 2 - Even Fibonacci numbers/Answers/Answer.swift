struct fib {
    private var value = 0
    private var (a, b) = (1, 2)

    init (limit: Int) {
        self.value = limit
    }

    mutating func getNext() -> Int? {
        while (a < value) {
            (a, b) = (b, b+a)
            return a
        }
        return nil
    }

    mutating func current() -> Int {
        return a
    }
}

print("Enter a number: ", terminator: "")
let limit = Int(readLine()!)
var summation: Int = 0
var value = fib(limit: limit!)
while (value.getNext() != nil) {
    if (value.current() % 2 == 0) {
        summation = summation + value.current()
    }
}
print(summation)