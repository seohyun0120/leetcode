/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {number} a
 * @param {number} b
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeInBetween = function(list1, a, b, list2) {
    let cnt = 1;
    let cur = list1;
    
    while (cnt < a) {
        cur = cur.next;
        cnt++;
    }
    const prev1 = cur;
    
    while (cnt <= b) {
        cur = cur.next;
        cnt++;
    }
    const prev2 = cur;

    cur = list2;
    while (cur !== null && cur.next !==null) {
        cur = cur.next;
    }
    
    prev1.next = list2;
    cur.next = prev2.next;
    
    return list1;
};