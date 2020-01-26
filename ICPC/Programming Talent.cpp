#include <iostream>
#include <fstream>

using namespace std;


int abs(int num) {
	if (num < 0)
		return num * -1;
	else
		return num;
}

void function() {
	ifstream readData;
	readData.open("P5_input.txt");
	int count = 0;
	int j;
	int c;
	int temp;
	int temp1;
	while(!readData.eof()){
		count++;
		readData >> c;
		readData >> j;
		
		int array[j][c];
		
		for(int i = 0; i < j; i++) {
			for(int k = 0; k < c; k++) {
				
				array[i][k] = 0;
			}
		}
		
		for(int i = 0; i < j; i++) {
			for(int k = 0; k < 2; k++) {
				readData >> temp;
				temp1 = abs(temp);
				array[i][temp1 - 1] = temp;
			}
		}
		
		int ans[c];
		
		for(int k = 0; k < c; k++) {
			ans[k] = 0;
		}
		
		bool flag = true;
		for(int i = 0; i < c; i++) {
			for(int k = 0; k < j; k++) {
				ans[i] += array[k][i];
			}
			if(ans[i] > 0){
				flag = false;
				cout << "Case "<< count <<": Yes" << endl;
				break;
			}
		}
		if(flag == true){
			cout << "Case "<< count <<": No" << endl;
			
		}
		
	}
	
	readData.close();
	
}
	

int main() {
	function();
}
