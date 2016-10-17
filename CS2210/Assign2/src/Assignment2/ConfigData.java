package Assignment2;
/**
 * Created by tambe on 2016/10/2.
 */
public class ConfigData {
    String config;
    int score;
    public ConfigData(String config, int score){
        this.config = config;
        this.score = score;
    }

    public String getConfig(){
        return this.config;
    }

    public int getScore(){
        return this.score;
    }

}
