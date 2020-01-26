#include <iostream>
#include <fstream>

using namespace std;


void countStrokes() {
	ifstream readData;
	readData.open("P1_input.txt");
	int count = 0;
	int strokes = 0;
	char board[8][8];
	
	for(int i = 0; i < 8; i++) {
		for(int j = 0; j < 8; j++) {
			readData >> board[i][j];
		}
	}
	
	for(int i = 0; i < 8; i++) {
		count = 0;
		for(int j = 0; j < 8; j++) {
			if(board[i][j] == 'B') {
				count++;
			}
			else{
				count = 0;
			}
		}
		
		if (count == 8) {
			strokes++;
		}
	}
	
	
	if (strokes != 8) {
		
	count = 0;
	
	for(int i = 0; i < 8; i++) {
		count = 0;
		for(int j = 0; j < 8; j++) {
			if(board[j][i] == 'B') {
				count++;
			}
			else{
				count = 0;
			}
		}
		
		if (count == 8) {
			strokes++;
		}
	}
	}
	
	cout << "Case 1: " << strokes;
	
	readData.close();

}


int main() {
	countStrokes();
}
