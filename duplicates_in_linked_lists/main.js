const { createLinkedList, traverse } = require("./utils");

function removeDuplicatesFromLinkedList(linkedList) {
  // Write your code here.

  let current = linkedList;
  while (current.next) {
    next_node = current.next;
    current.value === next_node.value
      ? (current.next = next_node.next)
      : (current = current.next);
  }

  return traverse(linkedList);
}

const arr = [1, 1, 3, 4, 4, 4, 5, 6, 6, 6];
const head = createLinkedList(arr);
console.log(traverse(head));
console.log(removeDuplicatesFromLinkedList(head));
