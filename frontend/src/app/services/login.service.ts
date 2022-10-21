import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Student } from '../models/student';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private http: HttpClient) { }
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error);
      return of(result as T);
    };
  }

  private baseURL = `http://127.0.0.1:8000/api/user`;

  getToken(id:string, password:string): Observable<any> {
    const url = `${this.baseURL}/login?id=${id}&password=${password}`;
    return this.http
      .get<any>(url)
      .pipe(catchError(this.handleError<any>()));
  }

  loginByToken(): Observable<any> {
    const url = `${this.baseURL}/login?token=${localStorage.getItem('token')}`;
    return this.http
      .get<Student>(url)
      .pipe(catchError(this.handleError<Student>()));
  }

  Logout() {
    const url = `${this.baseURL}/logout/${localStorage.getItem('token')}`;
    return this.http
      .delete<any>(url)
      .pipe(catchError(this.handleError<any>()));
  }
}
