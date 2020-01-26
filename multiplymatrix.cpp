#include <iostream>
#include <fstream>

using namespace std;

void multiplyMatrix(int n) {
	ifstream readData;
	readData.open("p2_input.txt");
	
	int x1,y1;
	int x2,y2;
	if(readData.is_open()){
		for(int i = 0; i <n; i++){
			string a;
			getline(readData, a);
		}
		readData >> x1;
		readData >> y1;
		int M[x1][y1];
		for(int i = 0; i < x1; i++){
			for(int j = 0; j < y1; j++){
				readData >> M[i][j];
			}
		}
		
		readData >> x2;
		readData >> y2;
		int N[x2][y2];
		for(int i = 0; i < x2; i++){
			for(int j = 0; j < y2; j++){
				readData >> N[i][j];
			}
		}
		
		if(y1 == x2){
			//multiply
			int A[x2][y1];
			
			for(int i = 0; i < x2; i++){
				for(int j = 0; j < y1; j++){
					A[i][j] = 0;
				}
			}
			int Ans = 0;
			for(int i = 0; i < x2; i++){
				for(int j = 0; j < y1; j++){
					for(int k = 0; k < x2; k++){
						A[i][j] += M[i][k] * N[k][j];
					}
				}
			}
			
			for(int i = 0; i < x2; i++){
				for(int j = 0; j < y2; j++){
					Ans += A[i][j];
				}
			}
			
			cout << "Case# " << n << ": " << Ans << "\n";
		}
		else if(y1 == y2){
			//trans
			int array[y2][x2];
			
			
			
			int A[x2][y1+1];
			for(int i = 0; i < y1; i++){
				for(int j = 0; j < x1 + 1; j++){
					A[i][j] = 0;
				}
			}
			int Ans = 0;
			
			for(int i = 0; i < x2; i++){
				for(int j = 0; j < y2; j++){
					array[j][i] = N[i][j];
				}
			}
			for(int i = 0; i < x1; i++){
				for(int j = 0; j < x2; j++){
					for(int k = 0; k < y1; k++){
					
						A[i][j] += M[i][k] * array[k][j];
					}
				}
			}
			
			for(int i = 0; i < x2; i++) { 
				A[i][x2] = A[i][0];
			}
			
			for(int i = 0; i < x2; i++){
				for(int j = 0; j <= x2; j++){
					Ans += A[i][j];
				}
			}
			
			cout << "Case# " << n << ": " << Ans << "\n";
		}
		else{
			// not possible
			
			cout << "Case# " << n << ": " << "Not possible" << "\n";
		}	
	
	readData.close();
	}
	else{
		cout << "file is not open" << endl;
	}
}

int main() {
	int num;
	ifstream in;
	in.open("p2_input.txt");
	in >> num;
	in.close();
	for(int i = 1; i <= num; i++){
		multiplyMatrix(i);
	}
	
	
}
