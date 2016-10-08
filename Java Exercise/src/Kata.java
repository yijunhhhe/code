class Kata {
    public static String getMiddle(String word) {
        if (word.length % 2 == 0)
        {return (word.substring(word.length/2 - 1, word.length / 2));}
        else{
            return (Character.toString(word.charAt(word.length/2)));}
    }
    public static void main (String[] args){
        System.out.println(getModdle("hello"));
    }
}