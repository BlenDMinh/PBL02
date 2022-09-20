#include"Student.h"
#include"IOUtility.h"

Student::Student() {

}

Student::Student(std::string studentName, std::string studentClass, std::string studentId) {
    name = studentName;
    mainClass = studentClass;
    id = studentId;
}

Student::~Student() {

}

std::string Student::GetName() {
    return name;
}

std::string Student::GetClass() {
    return mainClass;
}
std::string Student::GetId() {
    return id;
}

void Student::LoadFromFile(std::string path) {

}

std::vector<Student> Student::LoadFromCSV(std::string path) {
    std::vector<Student> studentList;

    auto data = ReadCSV(path);
    for(auto row : data)
        studentList.push_back(Student(row[2], row[3], row[1]));
    return studentList;
}

static std::string ConvertToHTMLTable(std::vector<Student> studentList) {
    return "";
}