function binarySearch(array, target, start=0, end=array.length-1) {
    // Write your code here.
    const mid = parseInt((start+end)/2);
    if(array[mid] === target) {
      return mid;
    } else if(start === end) {
      return -1;
    } else if(target < array[mid]) {
      return binarySearch(array, target, start, mid-1);
    } else {
      return binarySearch(array, target, mid+1, end);
    }
  }
  
  // Do not edit the line below.
  exports.binarySearch = binarySearch;
  