function* fib (limit) {
    [a, b] = [1, 2]
    while (a < limit) {
        [a, b] = [b, a+b]
        yield a
    }
}

function mainModule(upper_bound) {
    summation = 0
    for (let value of fib(upper_bound)) {
        if (value % 2 == 0) {
            summation += value
        }
    }
    return summation
}

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

readline.question(`Enter a number: `, value => {
    console.log(mainModule(+value))
    readline.close();
});