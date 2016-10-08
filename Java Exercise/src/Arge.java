
class Arge {

    public static int nbYear(int p0, double percent, int aug, int p) {
        int n = 1;
        double total = 0;
        total = p0 * percent + p0 + aug;
        while (total <= p) {
            total = total + total * (percent/100) + aug;
            n++;
        }
        return n;
    }

    public static void main (String[] args){
        System.out.println(nbYear(1500, 5, 100, 5000));
    }
}