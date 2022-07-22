package leetcode.java.algorithms;

import java.util.*;

public class leetcode86 {

     public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next;
        }
     }

    class Solution {
        public ListNode partition(ListNode head, int x) {

            Stack<ListNode> lower = new Stack<>();
            Stack<ListNode> higher = new Stack<>();

            while (head != null) {
                if (head.val < x) {
                    lower.push(head);
                } else {
                    higher.push(head);
                }
                head = head.next;
            }

            // higher stack
            head = null;
            while (!higher.isEmpty()) {
                ListNode node = higher.pop();
                node.next = head;
                head = node;
            }

            // lower stack
            while (!lower.isEmpty()) {
                ListNode node = lower.pop();
                node.next = head;
                head = node;
            }

            return head;
        }
    }
}