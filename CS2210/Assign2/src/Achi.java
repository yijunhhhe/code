
/**
 * Created by tambe on 10/9/2016.
 */
public class Achi {
    char[][] gameBoard;

    int board_size;
    public Achi(int board_size, int max_levels){
        gameBoard = new char[board_size][board_size];
        this.board_size = board_size;
        for ( int i = 0; i < board_size; i++){
            for(int j = 0; j < board_size; j++){
                gameBoard[i][j] = ' ';
            }
        }
    }

    public Dictionary createDictionary(){
        return new Dictionary(13937);
    } 

    public int repeatedConfig(Dictionary configurations) {
        StringBuilder config = new StringBuilder();
        for (int i = 0; i < board_size; i++) {
            for (int j = 0; j < board_size; j++) {
                config.append(gameBoard[i][j]);
            }
        }
        return configurations.find(config.toString());
    }

    public void insertConfig(Dictionary configurations, int score){
        StringBuilder config = new StringBuilder();
        for (int i = 0; i < board_size; i++) {
            for (int j = 0; j < board_size; j++) {
                config.append(gameBoard[i][j]);
            }
        }
        ConfigData newConfig = new ConfigData(config.toString(), score);
        try {
			configurations.insert(newConfig);
		} catch (DictionaryException e) {
			e.printStackTrace();
		}
    }

    public void storePlay(int row, int col, char symbol){
    	gameBoard[row][col] = symbol;
    }
    
    public boolean tileIsEmpty(int row, int col){
        if (gameBoard[row][col] == ' '){
        	return true;
        }
        return false;
    }

    public boolean tileIsComputer(int row, int col){
        if(gameBoard[row][col] == 'O'){
        	return true;
        }
        return false;
    }

    public boolean tileIsHuman(int row, int col){
    	if(gameBoard[row][col] == 'X'){
        	return true;
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
        //row win
        while (size < board_size * board_size){
            if (config1.substring(size, size + board_size).equals(newSymbol) ){
                return true;
            }
            size = size + board_size;
        }

        // column win
        StringBuilder config2 = new StringBuilder();
        for (j = 0; j < board_size; j++) {
            for (i = 0; i < board_size; i++) {
                config2.append(gameBoard[i][j]);
            }
        }
        size = 0;
        while (size < board_size * board_size){
            if(config2.substring(size, size + board_size).equals(newSymbol)){
                return true;
            }
            size = size + board_size;
        }

        //diagonal
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
        while(size < board_size * 2){
            if(config3.substring(size, size + board_size).equals(newSymbol)){
                return true;
            }
            size = size + board_size;
        }

        return false;
    }

    public boolean isDraw(char symbol){
        int row = 0, column = 0;
        int count = 0;
        for (int i = 0; i < board_size; i++) {
            for (int j = 0; j < board_size; j++) {
                if(gameBoard[i][j] == ' '){
                    row = i;
                    count++;
                    column = j;
                    
                }
            }   
        }
        if (count > 1){
        	return false;
        }
        if(row == 0 && column == 0){
            if(gameBoard[1][0] != symbol && gameBoard[0][1] != symbol && gameBoard[1][1] != symbol){
                return true;
            }
        } else if(row == board_size - 1 && column == 0){
            if(gameBoard[board_size-2][0] != symbol && gameBoard[board_size -2][1] != symbol && gameBoard[board_size - 1][1] != symbol){
                return true;
            }
        } else if(row == 0 && column == board_size - 1){
            if(gameBoard[0][board_size -2] != symbol && gameBoard[1][board_size -2] != symbol && gameBoard[1][board_size -1] != symbol)
                return true;
        } else if(row == board_size - 1 && column == board_size - 1 ){
            if(gameBoard[board_size - 1][board_size - 2] != symbol && gameBoard[board_size - 2][board_size - 2] != symbol && gameBoard[board_size - 2][board_size - 1] != symbol)
                return true;
        } else if(row == 0 && column != board_size - 1 && column != 0){
        	if(gameBoard[row][column - 1] != symbol && gameBoard[row][column + 1] != symbol){
        		if(gameBoard[row + 1][column - 1] != symbol && gameBoard[row + 1][column] != symbol && gameBoard[row + 1][column + 1] != symbol){
        		return true;}
        	}
        } else if(row == board_size && column != board_size - 1 && column != 0){
        	if(gameBoard[row - 1][column - 1] != symbol && gameBoard[row -1][column] != symbol && gameBoard[row - 1][column + 1] != symbol ){
        		if(gameBoard[row][column - 1] != symbol && gameBoard[row][column + 1] != symbol){
        		return true;}
        	}
        } else if(column == 0 && row != board_size - 1 && row != 0){
        	if(gameBoard[row - 1][column] != symbol && gameBoard[row + 1][column] != symbol){
        		if(gameBoard[row - 1][column + 1] != symbol && gameBoard[row][column + 1] != symbol && gameBoard[row + 1][column + 1] != symbol){
        			return true;
        		}
        	}
        } else if(column == board_size - 1 && row != board_size - 1 && row != 0){
        	if(gameBoard[row - 1][column - 1] != symbol && gameBoard[row][column - 1] != symbol && gameBoard[row + 1][column - 1] != symbol){
        		if(gameBoard[row - 1][column] != symbol && gameBoard[row + 1][column] != symbol){
        			return true;
        		}
        	}
        } else if(gameBoard[row - 1][column - 1] != symbol && gameBoard[row -1][column] != symbol && gameBoard[row - 1][column + 1] != symbol){
        	if(gameBoard[row][column - 1] != symbol && gameBoard[row][column + 1] != symbol){
        		if(gameBoard[row + 1][column - 1] != symbol && gameBoard[row + 1][column] != symbol && gameBoard[row + 1][column + 1] != symbol){
        			return true;
        		}
        	}
        }
        return false;
    }

    public int evalBoard(char symbol){
        if (wins(symbol) == true){
            if (symbol == 'O'){
                return 3;
            }else {
                return 0;
            }
        }else if(isDraw(symbol) == true){
            return 2;
        }else{
            return 1;
        }

    }
}

//boolean a = gameBoard[row - 1][column - 1] != symbol && gameBoard[row -1][column] != symbol && gameBoard[row - 1][column + 1] != symbol ;
//  boolean b = gameBoard[row][column - 1] != symbol && gameBoard[row][column + 1] != symbol;
//  boolean c = gameBoard[row + 1][column - 1] != symbol && gameBoard[row + 1][column] != symbol && gameBoard[row + 1][column + 1] != symbol;
//boolean d = gameBoard[row - 1][column - 1] != symbol && gameBoard[row][column - 1] != symbol && gameBoard[row + 1][column - 1] != symbol;
//boolean e = gameBoard[row - 1][column] != symbol && gameBoard[row + 1][column] != symbol;
//boolean f = gameBoard[row - 1][column + 1] != symbol && gameBoard[row][column + 1] != symbol && gameBoard[row + 1][column + 1]!= symbol;
