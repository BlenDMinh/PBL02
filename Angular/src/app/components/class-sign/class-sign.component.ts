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

  timetable = new Array<boolean>(7 * 15);

  classes: Class[] = [];
  newClasses: Class[] = [];
  timetableConflict: boolean[] = [];

  ngOnInit(): void {
    this.loginService.loginByToken().subscribe((student) => {
      this.loginUser = student;
      if (this.loginUser.hasOwnProperty('error')) {
        location.replace('/main');
      }

      this.classSectionService
        .getClassesAttendedByStudent(this.loginUser['studentId'])
        .subscribe((data) =>
          (this.classes = data).sort((n1, n2) => {
            if (n1.sectionID > n2.sectionID) {
              return 1;
            }
            if (n1.sectionID < n2.sectionID) {
              return -1;
            }
            return 0;
          })
        );

      this.classSectionService
        .getNewClasses(this.loginUser['studentId'])
        .subscribe((data) => {
          this.newClasses = data;

          this.classes.forEach(element => {
            for(let i = element.startTime; i <= element.endTime; i++)
              this.timetable[i] = true;
          });
          this.timetableConflict = new Array<boolean>(this.newClasses.length);
          for(let i = 0; i < this.newClasses.length; i++) {
            let flag = false;
            for(let j = this.newClasses[i].startTime; j <= this.newClasses[i].endTime; j++)
              if(this.timetable[j]) {
                flag = true;
                break;
              }
            this.timetableConflict[i] = flag;
          }
        });
    });
  }

  addClassSection(section: Class, student: Student): void {
    this.classSectionService.addClass(section, student);
    location.replace('/classSign');
  }

  deleteClassSection(section: Class, student: Student): void {
    this.classSectionService.deleteClass(section.sectionID, student.studentId);
    location.replace('/classSign');
  }
}
