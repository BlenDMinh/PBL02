import { Component, OnInit } from '@angular/core';
import { LoginService } from 'src/app/services/login.service';

@Component({
  selector: 'app-class-sign',
  templateUrl: './class-sign.component.html',
  styleUrls: ['./class-sign.component.scss'],
})
export class ClassSignComponent implements OnInit {
  loginUser: any;
  link = 'classSign';

  constructor(private loginService: LoginService) {}

  ngOnInit(): void {
    this.loginService.loginByToken().subscribe((student) => {
      this.loginUser = student;
      if (this.loginUser.hasOwnProperty('error')) {
        location.replace('/main');
      }
    });
  }
}