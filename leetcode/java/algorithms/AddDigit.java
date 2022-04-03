package leetcode.algorithms;

// https://leetcode.com/problems/add-digits/submissions/
// #258 Add Digits
public class AddDigit {
    public int addDigits(int num) {
        int sum = 0;
        int input = num;
        while (true) {
            sum = 0;
            String inputStr = Integer.toString(input);
            for (int i = 0; i < inputStr.length(); i++) {
                sum += inputStr.charAt(i) - '0';
            }
            if (Integer.toString(sum).length() == 1) {
                break;
            }
            input = sum;
        }
        return sum;
    }

    public static void main(String[] args) {
        AddDigit addDigit = new AddDigit();
        System.out.println(addDigit.addDigits(38));
    }
}
