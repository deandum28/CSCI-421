#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <openssl/md5.h>

using namespace std;

typedef unsigned char BYTE;

int main()
{
    cout << endl << endl;
    for(unsigned int i = 0; i < 16581375; i++) {
        BYTE a, b, c; //to store byte by byte value
    
        a = (i&0xFF); //extract first byte
        b = ((i>>8)&0xFF); //extract second byte
        c = ((i>>16)&0xFF); //extract third byte
        
        unsigned char output[16] = {};
        MD5((const unsigned char*)&i, 3, output); // generate md5
        
        if (a == output[0] && b == output[1] && c == output[2]) {
            // cout << "working\n";
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
