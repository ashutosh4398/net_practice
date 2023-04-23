function getNthFib(n) {
    // Write your code here.
    //   n here is nth number
    // eg if fibo series is 0,1,1,2,3,5,8
    // n==1 represents 0th index
    // n==2 represents 1st index hence the base condition
    if (n === 1) return 0;
    if (n === 2) return 1;
    return getNthFib(n - 1) + getNthFib(n - 2);
}


console.log(getNthFib(6));

// Do not edit the line below.
exports.getNthFib = getNthFib;