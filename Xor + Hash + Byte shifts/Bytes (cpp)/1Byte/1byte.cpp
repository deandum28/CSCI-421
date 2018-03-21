#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <openssl/md5.h>

using namespace std;

int main()
{
    cout << endl << endl;
    for(unsigned char i = 0; i < 255; i++) {
        unsigned char output[16] = {};
        MD5((const unsigned char*)&i, 1, output);
        if(i == output[0]) {
            cout << "Found one! \n";
            printf("Value: %u\n", i);
            cout << "Hash: ";
            for(int i = 0; i < 16; i++){
                 printf("%02X", output[i]);
            }
            cout << endl << endl;
        }
    }
    return 0;
}