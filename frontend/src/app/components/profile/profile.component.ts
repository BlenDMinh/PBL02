import { Component, OnInit } from '@angular/core';
import { Student } from 'src/app/models/student';
import { LoginService } from 'src/app/services/login.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss'],
})
export class ProfileComponent implements OnInit {
  students: Student[] = [];
  loginUser: any;
  link = 'profile';
  constructor(private loginService: LoginService) {}

  ngOnInit(): void {
    this.loginService.loginByToken().subscribe((student) => {
      this.loginUser = student;
    });
  }
}
