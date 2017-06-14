/*
 * MinimaxPlayer.cpp
 *
 *  Created on: Apr 17, 2015
 *      Author: wong
 */
#include <iostream>
#include <assert.h>
#include <climits>
#include "MinimaxPlayer.h"

using std::vector;

MinimaxPlayer::MinimaxPlayer(char symb) :
		Player(symb) {

}

MinimaxPlayer::~MinimaxPlayer() {

}

void MinimaxPlayer::get_move(OthelloBoard* b, int& col, int& row) {
    // To be filled in by you
    OthelloBoard temp_b = clone_OthelloBoard(*b);
    Action act = alpha_beta_search(temp_b, this->get_symbol());
    col = act.column;
    row = act.row;
}

Action MinimaxPlayer::alpha_beta_search(OthelloBoard b, char symbol){
	int value, result_value = INT_MAX, alpha = INT_MIN, beta = INT_MAX;
	Action_List act_list = successors(b, symbol);
	Action a, result;
	
	for(int i = 0; i < act_list.size; i++){
		OthelloBoard temp_b = clone_OthelloBoard(b);
		a = act_list.act[i];
		temp_b.play_move(a.column, a.row, symbol);
		value = max_value(temp_b, alpha, beta, symbol);
		if(value < result_value)
			result = a;
			result_value = value;		
	}
	return result;
}

int MinimaxPlayer::max_value(OthelloBoard b, int& alpha, int& beta, char symbol){
	symbol = change_symbol(symbol);
	if((terminal_test(b, symbol)))
		return unility(b);

	int v = INT_MIN;
	Action_List act_list = successors(b, symbol);
	Action a;

	for(int i = 0; i < act_list.size; i++){
		OthelloBoard temp_b = clone_OthelloBoard(b);
		a = act_list.act[i];
		temp_b.play_move(a.column, a.row, symbol);
		v = max(v, min_value(temp_b, alpha, beta, symbol));
		if(v >= beta)
			return v;
		alpha = max(alpha, v);
	}
	return v;
}
 
int MinimaxPlayer::min_value(OthelloBoard b, int& alpha, int& beta, char symbol){
	symbol = change_symbol(symbol);
	if((terminal_test(b, symbol)))
		return unility(b);

	int v = INT_MAX;
	Action_List act_list = successors(b, symbol);
	Action a;

	for(int i = 0; i < act_list.size; i++){
		OthelloBoard temp_b = clone_OthelloBoard(b);
		a = act_list.act[i];
		temp_b.play_move(a.column, a.row, symbol);
		v = min(v, max_value(temp_b, alpha, beta, symbol));
		if(v <= alpha)
			return v;
		beta = min(beta, v);
	}
	return v;
}

bool MinimaxPlayer::terminal_test(OthelloBoard b, char symbol){
	return !b.has_legal_moves_remaining(symbol);
}

int MinimaxPlayer::unility(OthelloBoard b){
	return b.count_score(b.get_p1_symbol()) - b.count_score(b.get_p2_symbol());
}

Action_List MinimaxPlayer::successors(OthelloBoard b, char symbol){
	Action_List act_list;
	act_list.size = 0;
	act_list.capacity = 5;
	act_list.act = (Action*)malloc(5*sizeof(Action));

	for (int c = 0; c < b.get_num_cols(); c++) {
		for (int r = 0; r < b.get_num_rows(); r++) {
			if(b.is_legal_move(c, r, symbol)){
				act_list.act[act_list.size].column = c;
				act_list.act[act_list.size].row = r;
				act_list.size += 1;

				if(act_list.size == act_list.capacity){
					act_list.act = expand_capacity(act_list); 
					act_list.capacity = 2 * act_list.capacity;
				}
			}
		}
	}	
	return act_list;
}

int MinimaxPlayer::max(int num1, int num2){
	if(num1 > num2)
		return num1;
	else
		return num2;
}

int MinimaxPlayer::min(int num1, int num2){
	if(num1 > num2)
		return num2;
	else
		return num1;
}

Action* MinimaxPlayer::expand_capacity(Action_List act_list){
	int c = act_list.capacity;
	Action* act = (Action*)malloc(2*c*sizeof(Action));
	for(int i = 0; i < act_list.size; i++)
		act[i] = act_list.act[i];
	return act;
}

char MinimaxPlayer::change_symbol(char symbol){
	if(symbol == 'X')
		return 'O';
	else
		return 'X';
}

OthelloBoard MinimaxPlayer::clone_OthelloBoard(OthelloBoard b){
	OthelloBoard temp(b.get_num_cols(), b.get_num_rows(), b.get_p1_symbol(), b.get_p2_symbol());
	for(int i = 0; i < b.get_num_cols(); i++)
		for(int j = 0; j < b.get_num_rows(); j++)
			temp.set_cell(i, j, b.get_cell(i, j));
	return temp;
}

MinimaxPlayer* MinimaxPlayer::clone() {
	MinimaxPlayer* result = new MinimaxPlayer(symbol);
	return result;
}