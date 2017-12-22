#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
    string line = "";
    for(int i = 0; i < argc; i = i + 1)
    {
        line += string(argv[i])+" ";
    }
    system("python compile.py "+string(line));
    return 0;
}