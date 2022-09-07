#pragma once
#include<string>
#include<vector>

class Student {
private:
    std::string name, mainClass, id;
public:
    Student();
    Student(std::string, std::string, std::string);
    ~Student();

    std::string GetName();
    std::string GetClass();
    std::string GetId();

    void LoadFromFile(std::string);
    static std::vector<Student> LoadFromCSV(std::string);
    static std::string ConvertToHTMLTable(std::vector<Student>);
};