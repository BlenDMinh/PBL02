import { Component, OnInit } from '@angular/core';
import { LoginService } from 'src/app/services/login.service';

@Component({
  selector: 'app-timetable',
  templateUrl: './timetable.component.html',
  styleUrls: ['./timetable.component.scss'],
})
export class TimetableComponent implements OnInit {
  table: [string, number][][] = [[], 
  [['OOP', 3], ['OOP', 3], ['OOP', 3], ['OOP', 3], ['OOP', 3], ['OOP', 3]], 
  [['#', 0], ['#', 0], ['#', 0], ['#', 0], ['#', 0], ['#', 0]], 
  [['#', 0], ['#', 0], ['#', 0], ['#', 0], ['#', 0], ['#', 0]], 
  []]
  loginUser: any;
  link = 'timetable';
  today = new Date()

  constructor(private loginService: LoginService) {}

  ngOnInit(): void {
    this.loginService.loginByToken().subscribe((student) => {
      this.loginUser = student;
      if (this.loginUser.hasOwnProperty('error')) {
        location.replace('/main');
      }
    });
    console.log(this.today.getDay());
    
    // this.table[0] = [];
    // this.table[0][0] = ['a', 5];
    console.log(this.table[0][0] != undefined);
  }
}
