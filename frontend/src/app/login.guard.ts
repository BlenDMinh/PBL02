import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { LoginService } from './services/login.service';

@Injectable({
  providedIn: 'root',
})
export class LoginGuard implements CanActivate {
  constructor(private login: LoginService, private router: Router) {}

  canActivate(): boolean {
    if (this.login.loginByToken()) return true;
    else {
      this.router.navigate(['/main']);
      return false;
    }
  }
}
