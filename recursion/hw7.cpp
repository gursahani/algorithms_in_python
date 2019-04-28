/*
 * File: hw7.cpp
 * Created at: 03/19/19, 13:22:13
 * Created by: Kunal Gursahani
 * Last Modified: 03/19/19, 15:10:57 
 * ------
 * Description: 
 * 
 * 
 */


#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<set>

using namespace std;


class hw7
{
private:
    /* data */
public:
    set<string> dictionary = {"hello","world"};
    vector<int, vector<int>> createMatrix(vector<int, vector<int>> v, string word, set<string> dictionary);
    string findValidWord(vector<int, vector<int>> v, string word, set<string> dictionary);
};

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}

vector<int,vector<int> > hw7::createMatrix(vector<int,vector<int> > v,string word,std::set<string> dictionary){
    for (int i = 0; i <= word.length(); i++) {
        for (int j = 0; j<=word.length(); j++) {
            if (dictionary.count(word.substr(i,j))) {
                v[i].push_back(1);
            }
        }
    }
    return v;
}



