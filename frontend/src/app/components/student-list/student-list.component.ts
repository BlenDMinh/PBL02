import { Component, OnInit } from '@angular/core';
import { main } from '@popperjs/core';
import { Student } from 'src/app/models/student';
import { StudentService } from 'src/app/services/student.service';

@Component({
  selector: 'app-student-list',
  templateUrl: './student-list.component.html',
  styleUrls: ['./student-list.component.scss'],
})
export class StudentListComponent implements OnInit {
  students: Student[] = [];
  link = 'main';

  constructor(private studentService: StudentService) {}

  getStudents(): void {
    this.studentService
      .getStudents()
      .subscribe((students) => (this.students = students));
  }

  ngOnInit(): void {
    this.getStudents();
  }
}
