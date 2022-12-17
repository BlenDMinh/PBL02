import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Student } from '../models/student';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { BASE_URL } from './settings';

@Injectable({
  providedIn: 'root',
})
export class StudentService {
  constructor(private http: HttpClient) {}

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error);
      return of(result as T);
    };
  }

  private baseURL = BASE_URL + `/api/user/student/`;

  getStudents(): Observable<Student[]> {
    return this.http
      .get<Student[]>(this.baseURL)
      .pipe(catchError(this.handleError<Student[]>('getStudents', [])));
  }

  getStudent(id: String): Observable<Student> {
    const url = `${this.baseURL}/${id}`;
    return this.http
      .get<Student>(url)
      .pipe(catchError(this.handleError<Student>()));
  }
}
