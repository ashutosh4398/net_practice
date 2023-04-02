/* 
    TIME: O(nlogn) | space: O(n) [
        since we are using intermediate array for storing max values 
        and then reducing it
    ]
*/

const ASCENDING = 1;
const DESCENDING = 0;

const compareFunction = (order) => {
  return order === ASCENDING
    ? (a, b) => a - b
    : order === DESCENDING
    ? (a, b) => b - a
    : (a, b) => 0;
};

function tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) {
  // Write your code here.
  redShirtSpeeds.sort(compareFunction(ASCENDING));

  // to achieve max possible fastest, sort the arrays in opposite direction
  // to achieve min possible fastest, sort the arrays in same direction
  const blueOrdering = fastest ? DESCENDING : ASCENDING;
  blueShirtSpeeds.sort(compareFunction(blueOrdering));

  // iterate over both arrays
  let totalSpeed = redShirtSpeeds
    .map((redSpeed, index) => {
      const blueSpeed = blueShirtSpeeds[index];
      return Math.max(redSpeed, blueSpeed);
    })
    .reduce((accumulator, currentValue) => accumulator + currentValue, 0);

  return totalSpeed;
}

const redShirtSpeeds = [5, 5, 3, 9, 2];
const blueShirtSpeeds = [3, 6, 7, 2, 1];
const fastest = true;

console.log(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest));

// Do not edit the line below.
exports.tandemBicycle = tandemBicycle;
