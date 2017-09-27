//https://en.wikipedia.org/wiki/Levenshtein_distance#Iterative_with_two_matrix_rows
#include <iostream>
#include <string>
#include <vector>

int minimum(int a, int b, int c) {
	if (a >=b && a>=c) {
		return a;
	} else if (b >= a && b >= c) {
		return b;
	} else if (c >= a && c >= b) {
		return c;
	}
	return -1;
}

int calcDistance(std::string s1, std::string s2) {
	int l1 = s1.size();
	int l2 = s2.size();
	
	//handle empty strings
	if(l1 == 0) {
		return l2;
	}
	if(l2 == 0) {
		return l1;
	}

	//set up the vectors
	std::vector<int> v0(l2 + 1);
	std::vector<int> v1(l2 + 1);
	int subCost = 0;

	for(int i = 0; i < l2; i++) {
		v0[i] = i;
	}

	for(int i = 0; i < l1 - 1; i++) {
		v1[0] = i + 1;
		
		for (int j = 0; j < l2 - 1; j++) {
			if (s1[i] == s2[j]) {
				subCost = 0;
			} else {
				subCost = 1;
			}
			v1[j+1] = minimum(v1[j]+1, v0[j+1] +1, v0[j] +subCost);
		}
		v0 = v1;
	}
	return v0[l1];
}

int main(int argc, char *argv[]) {
	if(argc != 3) {
		std::cout << "Usage: " << argv[0] << "  string1 string2\n";
		return -1;
	}
	std::cout << calcDistance(argv[1], argv[2]) << std::endl;
}
