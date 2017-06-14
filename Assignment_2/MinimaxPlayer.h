/*
 * MinimaxPlayer.h
 *
 *  Created on: Apr 17, 2015
 *      Author: wong
 */

#ifndef MINIMAXPLAYER_H
#define MINIMAXPLAYER_H

#include "OthelloBoard.h"
#include "Player.h"
#include <vector>

struct Action {
	int row;
	int column;
};

struct Action_List {
	Action* act;
	int size;
	int capacity;
};

/**
 * This class represents an AI player that uses the Minimax algorithm to play the game
 * intelligently.
 */
class MinimaxPlayer : public Player {
public:

	/**
	 * @param symb This is the symbol for the minimax player's pieces
	 */
	MinimaxPlayer(char symb);

	/**
	 * Destructor
	 */
	virtual ~MinimaxPlayer();

	/**
	 * @param b   The board object for the current state of the board
	 * @param col Holds the return value for the column of the move
	 * @param row Holds the return value for the row of the move
	 */
    void get_move(OthelloBoard* b, int& col, int& row);

    /**
	 * @param b      The board object for the current state of the board
	 * @param symbol This is the symbol for the minimax player's pieces
	 * @return A action structure with column and row
	 */
    Action alpha_beta_search(OthelloBoard b, char symbol);
    
    /**
	 * @param b      The board object for the current state of the board
	 * @param alpha  Holds the value of alpha
	 * @param beta   Holds the value of beta
	 * @param symbol This is the symbol for the minimax player's pieces
	 * @return unility value
	 */
    int max_value(OthelloBoard b, int& alpha, int& beta, char symbol); 
    
     /**
	 * @param b      The board object for the current state of the board
	 * @param alpha  Holds the value of alpha
	 * @param beta   Holds the value of beta
	 * @param symbol This is the symbol for the minimax player's pieces
	 * @return unility value
	 */
    int min_value(OthelloBoard b, int& alpha, int& beta, char symbol); 
    
    /**
	 * @param b      The board object for the current state of the board
	 * @param symbol This is the symbol for the minimax player's pieces
	 * @return boolean value to determine terminal state
	 */
    bool terminal_test(OthelloBoard b, char symbol);
    
    /**
	 * @param b       The board object for the current state of the board
	 * @return unility value
	 */
    int unility(OthelloBoard b);
    
    /**
	 * @param b      The board object for the current state of the board
	 * @param symbol This is the symbol for the minimax player's pieces
	 * @return a action list structure storing all actions
	 */
    Action_List successors(OthelloBoard b, char symbol);
    
    /**
	 * @param num1 Holds a number 1
	 * @param num2 Holds a number 2
	 * @return a maximum number
	 */
    int max(int num1, int num2);
    
    /**
	 * @param num1 Holds a number 1
	 * @param num2 Holds a number 2
	 * @return a minimum number
	 */
    int min(int num1, int num2);
    
    /**
	 * @param act_list A action list structure storing all actions
	 * @return a number action list with double length
	 */
    Action* expand_capacity(Action_List act_list);
    
    /**
	 * @param symbol This is the symbol for the minimax player's pieces
	 * @return a symbol of another player
	 */
    char change_symbol(char symbol);

    /**
     * @param b The board object for the current state of the board
     * @return a copy of this othelloboard
     */
    OthelloBoard clone_OthelloBoard(OthelloBoard b);

    /**
     * @return A copy of the MinimaxPlayer object
     * This is a virtual copy constructor
     */
    MinimaxPlayer* clone();

private:

};


#endif
