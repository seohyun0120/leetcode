/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function(head, left, right) {
    if (left === right) {
        return head;
    }
    
    let cnt = 1;
    let beforeReverse = [];
    let reverse = [];
    let afterReverse = [];
    
    while (head) {
        if (cnt < left) {
            beforeReverse.push(head.val);
        }
        
        if (left <= cnt && cnt <= right) {
            reverse.unshift(head.val);
        }
        
        if (cnt > right) {
            afterReverse.push(head.val);
        }
        
        head = head.next;
        cnt++;
    }
    
    let result;
    let prev = null;
    
    while (afterReverse.length) {
        result = new ListNode(afterReverse.pop(), prev);
        prev = result;
    }
    
    while (reverse.length) {
        result = new ListNode(reverse.pop(), prev);
        prev = result;
    }

    
    while (beforeReverse.length) {
        result = new ListNode(beforeReverse.pop(), prev);
        prev = result;
    }

    return result;
};