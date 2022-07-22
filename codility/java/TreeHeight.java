package codility.java;

import java.util.*;

public class TreeHeight {
    class Solution {
        class Tree {
            public int x;
            public Tree l;
            public Tree r;
        }

        class Pair {
            Tree tree;
            int height;

            Pair(Tree tree, int height) {
                this.tree = tree;
                this.height = height;
            }
        }

        public int solution(Tree T) {
            // write your code in Java SE 8
            int answer = -1;

            if (T == null) {
                return answer;
            }

            Queue<Pair> queue = new LinkedList<>();
            queue.add(new Pair(T, 0));

            while (!queue.isEmpty()) {
                Pair cur = queue.poll();
                answer = cur.height;

                Tree left = cur.tree.l;
                Tree right = cur.tree.r;

                if (left != null) {
                    queue.add(new Pair(left, cur.height + 1));
                }
                if (right != null) {
                    queue.add(new Pair(right, cur.height + 1));
                }
            }
            return answer;
        }
    }
}
