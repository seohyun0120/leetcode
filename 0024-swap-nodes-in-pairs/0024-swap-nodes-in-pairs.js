/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    let temp = new ListNode(null, head);
    
    let cur = temp;

    while (cur.next && cur.next.next) {
        const one = cur.next;
        const two = cur.next.next;
        
        one.next = two.next;
        two.next = one;
        cur.next = two;
        
        cur = cur.next.next;
    }
    
    return temp.next;
};