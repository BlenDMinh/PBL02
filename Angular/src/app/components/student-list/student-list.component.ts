import { Component, OnInit } from '@angular/core';
import { Student } from 'src/app/models/student';
import { StudentService } from 'src/app/services/student.service';
import { LoginService } from 'src/app/services/login.service';

@Component({
  selector: 'app-student-list',
  templateUrl: './student-list.component.html',
  styleUrls: ['./student-list.component.scss'],
})
export class StudentListComponent implements OnInit {
  students: Student[] = [];
  loginUser: any;

  constructor(
    private studentService: StudentService,
    private loginService: LoginService
  ) {}

  getStudents(): void {
    this.studentService.getStudents().subscribe((students) =>
      (this.students = students).sort((n1, n2) => {
        if (n1.studentId > n2.studentId) {
          return 1;
        }
        if (n1.studentId < n2.studentId) {
          return -1;
        }
        return 0;
      })
    );
  }

  ngOnInit(): void {
    this.loginService.loginByToken().subscribe((student) => {
      this.loginUser = student;
    });
    this.getStudents();
  }
}
