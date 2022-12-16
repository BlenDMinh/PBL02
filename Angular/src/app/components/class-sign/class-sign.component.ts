import { Component, OnInit } from '@angular/core';
import { LoginService } from 'src/app/services/login.service';
import { Class } from 'src/app/models/class';
import { ClasssectionService } from 'src/app/services/classsection.service';
import { Student } from 'src/app/models/student';

@Component({
  selector: 'app-class-sign',
  templateUrl: './class-sign.component.html',
  styleUrls: ['./class-sign.component.scss'],
})
export class ClassSignComponent implements OnInit {
  loginUser: any;

  constructor(
    private loginService: LoginService,
    private classSectionService: ClasssectionService
  ) {}

  classes: Class[] = [];

  ngOnInit(): void {
    this.loginService.loginByToken().subscribe((student) => {
      this.loginUser = student;
      if (this.loginUser.hasOwnProperty('error')) {
        location.replace('/main');
      }

      this.classSectionService
        .getClassesAttendedByStudent(this.loginUser['studentId'])
        .subscribe((data) => {
          this.classes = data;
        });
    });
  }

  deleteClassSection(section: Class, student: Student): void {
    this.classSectionService.deleteClass(section.sectionID, student.studentId);
    location.replace('/classSign');
  }
}
