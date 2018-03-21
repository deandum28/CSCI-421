#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    string input_file = string(argv[1]);
    std::string key = (argv[2]);
    string output_file = "en-" + input_file;
    ifstream read(input_file.c_str(), std::ios::binary);
    ofstream print(output_file.c_str());
    char x;
    int i = 0;
    while (read.read(&x, 1))
    {
        x = x ^ key[i++];
        if(i == key.size()) {
            i = 0;
        } 
        print.write(&x, 1);
    }
    return 0;
}