#include <iostream>
#include <fstream>

using namespace std;

bool isPrime(int num){
	if(num < 2){
		return false;
	}
	for(int i = 2; i < num; i++){
		if(num % i == 0 ){
			return false;
		}
	}
	return true;
	
}
void numberGame(int n) {
	ifstream readData;
	readData.open("p3_input.txt");
	int num1, num2;
	if(readData.is_open()){
		for(int i = 0; i <n; i++){
			string a;
			getline(readData, a);
		}
		
		readData >> num1;
		readData >> num2;
		if(isPrime(num1) ){
			if(isPrime(num2)){
				cout << "Case# " <<n << ": " << num1+num2 << "\n";
			}
			else{
				cout << "Case# " <<n << ": " << num1*num2 << "\n";
			}
		}
		else if(isPrime(num2) ){
				cout << "Case# " <<n << ": " << num1*num2 << "\n";
			}
		else{
			cout << "Case# " <<n << ": not possible" << "\n";
		}
	}
		
	else{
		cout << "file is not open" << endl;
	}
	readData.close();
}

int main() {
	int num;
	ifstream in;
	in.open("p3_input.txt");
	in >> num;
	in.close();
	for(int i = 1; i <= num; i++){
		numberGame(i);
	}
	
	
}
