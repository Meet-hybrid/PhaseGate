public class PerfectSquareChecker {

    public static boolean isPerfectSquare(int n) {
        if (n < 0) return false;
        int number = 0;
        while (number * number <= n) {
            if (number * number == n) return true;
            number++;
        }
        return false;
    }

    public static boolean allPerfectSquares(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (!isPerfectSquare(arr[i])) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int[] testList = {4, 9, 25, 49};
        System.out.println(allPerfectSquares(testList)); 
    }
}
