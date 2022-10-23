import { Component, OnInit } from '@angular/core';
import { LoginService } from 'src/app/services/login.service';
import {
  FormBuilder,
  FormGroup,
  FormsModule,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';

@Component({
  selector: 'app-login-box',
  templateUrl: './login-box.component.html',
  styleUrls: ['./login-box.component.scss'],
})
export class LoginBoxComponent implements OnInit {
  loginForm: any;
  error: String = '';
  constructor(
    private formBuilder: FormBuilder,
    private loginService: LoginService
  ) {}

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group({
      id: ['', Validators.required],
      password: ['', Validators.required],
    });
  }
  Login() {
    if (this.loginForm.dirty && this.loginForm.valid) {
      this.loginService
        .getToken(this.loginForm.value.id, this.loginForm.value.password)
        .subscribe((data) => {
          if (data.hasOwnProperty('token')) {
            localStorage.setItem('token', data['token']);
            window.location.href = '/';
          } else {
            this.error = data['error'];
          }
        });
    }
  }
}
