const { Node } = require("./nodeStructure");

const createLinkedList = (array) => {
  let [head, prev] = [null, null];

  array.forEach((element) => {
    let current = new Node(element);
    if (!head) {
      head = current;
    }
    if (prev) {
      prev.next = current;
    }
    // last step to update prev
    prev = current;
  });
  return head;
};

const traverse = (head) => {
  let tempHead = head;
  let finalStr = "";
  while (tempHead.next) {
    finalStr += `${tempHead.value} -> `;
    tempHead = tempHead.next;
  }

  finalStr += tempHead.value;

  return finalStr;
};

module.exports = { createLinkedList, traverse };
