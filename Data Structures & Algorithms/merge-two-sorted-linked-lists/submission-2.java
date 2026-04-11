/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode list = new ListNode();
        ListNode temp1 = list;


        while(list1 != null){
            if(list2 != null && list2.val<list1.val){
                temp1.next = list2;
                list2 = list2.next;
            } else {
                temp1.next = list1;
                list1 = list1.next;
            }
            temp1 = temp1.next;
        }
        
        temp1.next = list2;

        return list.next;
        
    }
}