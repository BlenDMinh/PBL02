import { Component, OnInit, Input } from '@angular/core';
import { LoginService } from 'src/app/services/login.service';
import { Student } from 'src/app/models/student'

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
})
export class NavbarComponent implements OnInit {
  @Input() active?: string;
  @Input() loginName?: String;
  constructor(private loginService : LoginService) {}

  ngOnInit(): void {

  }

  Logout() {
    this.loginService.Logout().subscribe();
    location.reload();
  }
}
