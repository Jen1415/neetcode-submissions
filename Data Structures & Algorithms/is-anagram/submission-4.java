
public class Solution {
    public static void main(String[] args) {
        System.out.println(isAnagram("jam", "ajm"));
    }

    public static boolean isAnagram(String s, String t) {
        // check the length
        if(s.length() != t.length()) return false;
        // sort the strings
        char[] characters = s.toCharArray();
        Arrays.sort(characters);
        String sSorted = new String(characters);
        characters = t.toCharArray();
        Arrays.sort(characters);
        String tSorted = new String(characters);

        return sSorted.equals(tSorted);
    }
}
