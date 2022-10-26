import { Injectable } from '@angular/core';
import { CanActivate } from '@angular/router';
import { LoginService } from './services/login.service';

@Injectable({
  providedIn: 'root',
})
export class LoginGuard implements CanActivate {
  constructor(private login: LoginService) {}

  canActivate(): boolean {
    if (this.login.loginByToken()) return true;
    else {
      location.replace('/main');
      return false;
    }
  }
}
