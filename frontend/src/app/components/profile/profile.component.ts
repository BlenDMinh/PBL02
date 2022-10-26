import { Component, OnInit } from '@angular/core';
import { LoginService } from 'src/app/services/login.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss'],
})
export class ProfileComponent implements OnInit {
  loginUser: any = null;
  link = 'profile';
  t = false;
  constructor(private loginService: LoginService) {}

  ngOnInit(): void {
    this.loginService.loginByToken().subscribe((student) => {
      this.loginUser = student;
      if (this.loginUser == null) {
        location.replace('/main');
      }
    });
  }
}
