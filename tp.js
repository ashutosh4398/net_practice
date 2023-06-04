const findFirstUniqueElem = (str) => {
    const visited = {};
    const uniqueElems = [];
    const uniqueElemsPos = {}

    let uniquePos = 0
    for(const i in str) {
        const char = str[i];
        if(visited[char] !== undefined){ 
            const uniquePos = uniqueElemsPos[char];
            uniqueElems[uniquePos] = "_";
        } else {
            visited[char] = i;
            uniqueElems.push(char);
            uniqueElemsPos[char] = uniquePos;
            uniquePos++;
        }
    }

    
    for(const elem of uniqueElems) {
        if(elem !== "_") {
            return uniqueElemsPos[elem];
        }
    }
    return -1;
}

console.log(findFirstUniqueElem("leetcode"))
console.log(findFirstUniqueElem("loveleetcode"))
console.log(findFirstUniqueElem("aabb"))