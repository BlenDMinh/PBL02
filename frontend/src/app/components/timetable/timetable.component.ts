import { Component, OnInit } from '@angular/core';
import { LoginService } from 'src/app/services/login.service';

@Component({
  selector: 'app-timetable',
  templateUrl: './timetable.component.html',
  styleUrls: ['./timetable.component.scss'],
})
export class TimetableComponent implements OnInit {
<<<<<<< Updated upstream
  loginUser: any = null;
=======
  table: [string, number][][] = [];
  loginUser: any;
>>>>>>> Stashed changes
  link = 'timetable';

  constructor(private loginService: LoginService) {}

  ngOnInit(): void {
    // this.table[0][0] = ['a', 0]
    this.loginService.loginByToken().subscribe((student) => {
      this.loginUser = student;
      if (this.loginUser.hasOwnProperty('error')) {
        location.replace('/main');
      }
    });
  }
}
