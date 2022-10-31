import { Component, OnInit } from '@angular/core';
import { LoginService } from 'src/app/services/login.service';

@Component({
  selector: 'app-timetable',
  templateUrl: './timetable.component.html',
  styleUrls: ['./timetable.component.scss'],
})
export class TimetableComponent implements OnInit {
  loginUser: any;
  link = 'timetable';

  constructor(private loginService: LoginService) {}

  ngOnInit(): void {
    this.loginService.loginByToken().subscribe((student) => {
      this.loginUser = student;
    });
  }
}
