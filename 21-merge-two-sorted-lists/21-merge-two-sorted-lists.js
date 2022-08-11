/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let head = null;
    let prev;
    
    while (list1 || list2) {
        let next;
        
        if (list1 && list2) {
            if (list1.val > list2.val) {
                next = list2;
                list2 = list2.next;
            } else {
                next = list1;
                list1 = list1.next;
            }
        } else if (list1) {
            next = list1;
            list1 = list1.next;
        } else if (list2) {
            next = list2;
            list2 = list2.next;
        }
        
        if (prev) {
            prev.next = next;
        }
        
        prev = next;
        
        if (!head) {
            head= next;
        }
    }
    
    return head;
};