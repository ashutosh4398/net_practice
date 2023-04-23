const productSum = (array, depth=1) => {
    // array can either contain interger or subarrays
    let depth_sum = 0;
    
    if ( Array.isArray(array) && array.length === 0 ) {
        return (1 * depth)
    }

    for(const element of array) {
        if (Array.isArray(element)) {
            depth_sum += productSum(element, depth+1);
        } else {
            depth_sum += element;
        }
    }

    return ( depth_sum * depth )
}
    

// arr = [1, [[]]]
arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

console.log(productSum(arr))