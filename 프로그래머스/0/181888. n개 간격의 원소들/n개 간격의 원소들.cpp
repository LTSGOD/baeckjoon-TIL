#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list, int n) {
    vector<int> answer;
    
    for(vector<int>::iterator iter = num_list.begin(); iter < num_list.end(); iter += n) {
        answer.push_back(*iter);
    }
    
    
    return answer;
}