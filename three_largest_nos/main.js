const insertAtPos = (arr, elem, pos) => {
    for(let i=0;i<pos; i++) {
        arr[i] = arr[i+1];
    }
    arr[pos] = elem;
}

const findThreeLargestNumbers = array => {
    const largestNos = [null, null, null];
    // largestNos = [141,1,17]
    for(const elem of array){
        for(let i=2; i>=0; i--) {
            if(!largestNos[i]) {
                largestNos[i] = elem;
                break;
            }
            if(largestNos[i] < elem) {
                insertAtPos(largestNos, elem, i);
                break;
            }
        }
    }

    return largestNos;
};


findThreeLargestNumbers([10,5,9,10,12]);