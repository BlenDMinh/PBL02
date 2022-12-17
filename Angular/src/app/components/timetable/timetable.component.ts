import { Component, OnInit } from '@angular/core';
import { LoginService } from 'src/app/services/login.service';
import { Class } from 'src/app/models/class';
import { ClasssectionService } from 'src/app/services/classsection.service';

@Component({
  selector: 'app-timetable',
  templateUrl: './timetable.component.html',
  styleUrls: ['./timetable.component.scss'],
})
export class TimetableComponent implements OnInit {
  table: [string, number][][] = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
  ];
  loginUser: any;
  today = new Date();

  private classes: Class[] = [];

  constructor(
    private loginService: LoginService,
    private classSectionService: ClasssectionService
  ) {}

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
          for (let i = 0; i < this.classes.length; i++) {
            const classSection = this.classes[i];
            var dayOfWeek: number = Math.floor(classSection.startTime / 15);
            var start = classSection.startTime % 15;
            var duration = classSection.endTime - classSection.startTime + 1;
            console.log(classSection, dayOfWeek, start, duration);
            this.table[start][dayOfWeek] = [classSection.subjectName, duration];
            for (let j = 1; j < duration; j++)
              this.table[start + j][dayOfWeek] = ['#', 0];
          }
        });
    });
  }
}
