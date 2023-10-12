// time complexity: O(l1log(l1) + (l2-l1)log(l1))
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        s1 = sort(s1);
        //Here i <= s2.length() - s1.length() ensures that the loop checks  all valid starting positions for a substring in s2 that has the same length as s1.
        for(int i=0; i <= s2.length() - s1.length(); i++){
            if(s1.equals(sort(s2.substring(i, i+ s1.length()))))
                return true;
        }
        return false; 
    }
    public String sort(String s) {
        char[] t = s.toCharArray();
        Arrays.sort(t);
        return new String(t);
    }
}