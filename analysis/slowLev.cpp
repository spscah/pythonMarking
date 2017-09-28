#include <iostream>

int min(int x, int y, int z){
    return std::min(std::min(x, y), z);
}

int distance(const char *s, int len_s, const char *t, int len_t) {
  int cost;

  if (len_s == 0) return len_t;
  if (len_t == 0) return len_s;

  if (s[len_s-1] == t[len_t-1])
      cost = 0;
  else
      cost = 1;

  return min(distance(s, len_s - 1, t, len_t    ) + 1,
             distance(s, len_s    , t, len_t - 1) + 1,
             distance(s, len_s - 1, t, len_t - 1) + cost);
}

int main(int argc, char * argv[]) {
	if(argc == 0) {
		std::cerr << "Usage\t" << argv[0] << " s1 s2" << std::endl;
		return -1;
	} else if(argc == 3) {
		std::cout << distance(argv[1], strlen(argv[1]), argv[2], strlen(argv[2])) << std::endl;
		return 0;
	} else {
		std::string a;
		std::string b;
		std::cin >> a;
		std::cin >> b;

		std::cout << distance(a.c_str(), a.size(), b.c_str(), b.size()) << std::endl;
		return 0;
	}
	return -1;
}
