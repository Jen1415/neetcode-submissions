


// find out if they have same length and same frequency of characters

public class Solution {
    public static void main(String[] args) {
        System.out.println(isAnagram("jam", "ajm"));
    }

    public static boolean isAnagram(String s, String t) {
        // check the length
        if(s.length() != t.length()) return false;
        HashMap<Character, Integer> sMap = new HashMap<>();
        HashMap<Character, Integer> tMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            sMap.put(s.charAt(i), sMap.getOrDefault(s.charAt(i), 0) + 1);
            tMap.put(t.charAt(i), tMap.getOrDefault(t.charAt(i), 0) + 1);
        }
        return sMap.equals(tMap);
    }
}