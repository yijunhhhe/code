/**
 * Created by tambe on 10/9/2016.
 */
public class Achi {
    char[][] gameBoard;

    int board_size;
    public Achi(int board_size, int max_levels){
        gameBoard = new char[board_size][board_size];
        this.board_size = board_size;
        for (i = 0; i < board_size; i++){
            for(j = 0; j < board_size; j++){
                gameBoard[i][j] = " ";
            }
        }
    }

    public Dictionary createDictionary(){
        return new Dictionary(10001);
    }

    public int repeatedConfig(Dictionary configurations) {
        StringBuilder config = new StringBuilder();
        for (i = 0; i < board_size; i++) {
            for (j = 0; j < board_size; j++) {
                config.append(gameBoard[i][j]);
            }
        }
        return configurations.find(config.toString());
    }

    public void insertConfig(Dictionary configurations, int score){
        StringBuilder config = new StringBuilder();
        for (i = 0; i < board_size; i++) {
            for (j = 0; j < board_size; j++) {
                config.append(gameBoard[i][j]);
            }
        }
        ConfigData newConfig = new ConfigData(config.tostring(), score);
        configurations.insert(newConfig);
    }

    public boolean tileIsEmpty(int row, int col){
        for (i = 0; i < board_size; i++) {
            for (j = 0; j < board_size; j++) {
                if (gameBoard[i][j] = " "){
                    return true;
                }
            }
        }
        return false;
    }

    public boolean titleIsComputer(int row, int col){
        for (i = 0; i < board_size; i++) {
            for (j = 0; j < board_size; j++) {
                if (gameBoard[i][j] = "O"){
                    return true;
                }
            }
        }
        return false;
    }

    public boolean tileIsHuman(int row, int col){
        for (i = 0; i < board_size; i++) {
            for (j = 0; j < board_size; j++) {
                if (gameBoard[i][j] = "X"){
                    return true;
                }
            }
        }
        return false;
    }

    public boolean wins(char symbol){
        StringBuilder config1 = new StringBuilder();
        int i,j;
        for (i = 0; i < board_size; i++) {
            for (j = 0; j < board_size; j++) {
                config1.append(gameBoard[i][j]);
            }
        }
        int size = 0;
        String newSymbol = new String(new char[board_size]).replace("\0", Character.toString(symbol));

        while (size <= board_size * board_size){
            if (config1.substring(size, size + board_size) == newSymbol){
                return true;
            }
            size = size + board_size;
        }

        StringBuilder config2 = new StringBuilder();
        for (j = 0; j < board_size; j++) {
            for (i = 0; i < board_size; i++) {
                config2.append(gameBoard[i][j]);
            }
        }
        size = 0;
        while (size <= board_size * board_size){
            if(config2.substring(size, size + board_size) == newSymbol){
                return true;
            }
            size = size + board_size;
        }

        StringBuilder config3 = new StringBuilder();
        for (i = 0; i < board_size; i++ ){
            config3.append(gameBoard[i][i]);
        }
        j = 0;
        for (i = board_size - 1 ; i >= 0; i--){
            config3.append(gameBoard[i][j]);
            j++;
        }
        size = 0;
        while(size <= board_size * board_size){
            if(config3.substring(size, size + board_size) == newSymbol){
                return true;
            }
            size = size + board_size;
        }

        return false;
    }

    public boolean isDraw(char sysmbol){
        int row = 0, column = 0;
        for (i = 0; i < board_size; i++) {
            for (j = 0; j < board_size; j++) {
                if(gameBoard[i][j] = " "){
                    row = i;
                    column = j;
                    break;
                }
            }
        }

        if(row == 0 && column == 0){

        }
    }


}
