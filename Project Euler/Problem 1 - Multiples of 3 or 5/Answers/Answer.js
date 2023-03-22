function multiples_of_3_and_5(limit) {
    limit = limit - 1
    const [limit3, limit5, limit15] = limits_for_3_5_and_15(limit)
    const [summation3, summation5, summation15] = summations_for_3_5_and_15(limit3, limit5, limit15)
    answer = summation3 + summation5 - summation15
    return answer
}

function limits_for_3_5_and_15(limit) {
    limit3 = Math.floor(limit/3)
    limit5 = Math.floor(limit/5)
    limit15  = Math.floor(limit/15)
    return [limit3, limit5, limit15]
}

function summations_for_3_5_and_15(limit3, limit5, limit15) {
    summation3 = 0.5*(limit3**2 + limit3)*3
    summation5 = 0.5*(limit5**2 + limit5)*5
    summation15 = 0.5*(limit15**2 + limit15)*15
    return [summation3, summation5, summation15]
}

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

readline.question(`Enter a number: `, value => {
    console.log(multiples_of_3_and_5(+value))
    readline.close();
});