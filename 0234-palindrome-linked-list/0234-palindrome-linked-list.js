/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    let arr = [];
    
    while (head) {
        arr.push(head.val);
        head = head.next;
    }
    
    let size = arr.length;
    
    let res = true;
    for (let i=0; i<size/2; i++) {
        if (arr.at(i) !== arr.at(size-i-1)) {
            res = false;
            break;
        };
    }

    return res;
};