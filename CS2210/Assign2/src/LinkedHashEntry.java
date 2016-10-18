
/**
 * Created by tambe on 2016/10/2.
 */
public class LinkedHashEntry {

    private ConfigData pair;

    LinkedHashEntry next;

    public LinkedHashEntry(ConfigData pair ){
        this.pair = pair;
    }

    public LinkedHashEntry getNext() {
        return next;
    }

    public void setNext(LinkedHashEntry next) {
        this.next = next;
    }

    public void setPair(ConfigData pair) {
        this.pair = pair;
    }

    public ConfigData getPair() {
        return pair;
    }
}
