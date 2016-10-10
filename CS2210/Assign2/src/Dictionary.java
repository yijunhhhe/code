/**
 * Created by tambe on 2016/10/2.
 */
public class Dictionary implements DictionaryADT{

    LinkedHashEntry[] table;


    public Dictionary(int size){
        table = new LinkedHashEntry[size];
    }

    public int insert(ConfigData pair) throws DictionaryException {

        char p = pair.getConfig().charAt(0);
        int accum = 33;
        int c = p;
        for (int i = 1; i < pair.getConfig().length(); i++){
            c = c + pair.getConfig().charAt(i)*accum;
            accum = accum * 33;
        }

        int hashCode = c % table.length;
        if(table[hashCode] == null) {
            table[hashCode] = new LinkedHashEntry(pair);
            return 0;
        }
        else {
            LinkedHashEntry entry = table[hashCode];
            while (entry.getNext() != null) {
                entry = entry.getNext();
            }
            entry.setNext(new LinkedHashEntry(pair));
            return 1;
        }
    }

    @Override
    public void remove(String config) throws DictionaryException {
        char p = config.charAt(0);
        int accum = 33;
        int c = p;
        for (int i = 1; i < config.length(); i++){
            c = c + config.charAt(i)*accum;
            accum = accum * 33;
        }

        int hashCode = c % table.length;
        if(table[hashCode] != null){
            LinkedHashEntry previous = null;
            LinkedHashEntry current = table[hashCode];
            while(current.getPair().getConfig() != config){
                previous = current;
                current = current.getNext();
            }
            if(previous == null){
                table[hashCode] = current.getNext();
            }else{
                previous.setNext(current.getNext());
            }
        }
    }

    @Override
    public int find(String config) {
        char p = config.charAt(0);
        int accum = 33;
        int c = p;
        for (int i = 1; i < config.length(); i++){
            c = c + config.charAt(i)*accum;
            accum = accum * 33;
        }

        int hashCode = c % table.length;
        if(table[hashCode] == null){
            return -1;
        }else{
            LinkedHashEntry entry = table[hashCode];
            while( entry.getPair().getConfig() != config && entry != null){
                entry = entry.getNext();
            }
            if (entry.getPair().getConfig() == config){
                return entry.getPair().getScore();
            }else{
                return -1;
            }
        }
    }
}
