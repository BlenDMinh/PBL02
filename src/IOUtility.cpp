#include "IOUtility.h"

std::vector<std::vector<std::string>> ReadCSV(std::string path) {
    std::fstream file(path, std::ios::in); 

    std::vector<std::vector<std::string>> content;
    std::vector<std::string> row;
    std::string line, word;

    if(file.is_open()) {
        while(getline(file, line)) {
            row.clear();
            std::stringstream str(line);
            while(getline(str, word, ','))
                row.push_back(word);
            content.push_back(row);
        }
    } else
        std::cout << "Could not open the file\n";

    return content;
}

std::string ReadAll(std::string path) {
    std::ifstream f(path); //taking file as inputstream
    std::string str;
    if(f) {
        std::ostringstream ss;
        ss << f.rdbuf(); // reading data
        str = ss.str();
    } else
        std::cout << "Could not open the file\n";
    return str;
}