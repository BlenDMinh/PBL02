import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Class } from '../models/class';
import { Student } from '../models/student';
import { BASE_URL } from './settings';

@Injectable({
  providedIn: 'root',
})
export class ClasssectionService {
  constructor(private http: HttpClient) {}

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error);
      return of(result as T);
    };
  }

  private baseURL = BASE_URL + `/api/classsection`;

  getClasses(): Observable<Class[]> {
    return this.http
      .get<Class[]>(this.baseURL)
      .pipe(catchError(this.handleError<Class[]>('getClasses', [])));
  }

  getClass(id: string): Observable<Class> {
    const url = this.baseURL + `/${id}`;

    return this.http
      .get<Class>(url)
      .pipe(catchError(this.handleError<Class>('getClasses')));
  }

  getClassesAttendedByStudent(studentID: string): Observable<Class[]> {
    const url = this.baseURL + `?sid=${studentID}`;

    return this.http
      .get<Class[]>(url)
      .pipe(
        catchError(this.handleError<Class[]>('getClassesAttendedByStudent', []))
      );
  }

  addClass(_class: Class, student: Student): void {
    const options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      }),
      body: {
        sid: student.studentId,
      },
    };
    const url = this.baseURL + `/${_class.sectionID}`;

    this.http.post(url, options).subscribe();
  }

  deleteClass(classID: string, studentID: Number): void {
    const options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      }),
      body: {
        sid: studentID,
      },
    };
    const url = this.baseURL + `/${classID}`;

    this.http
      .delete(url, options)
      .pipe(catchError(this.handleError<Class[]>('deleteClass', [])))
      .subscribe();
  }

  getNewClasses(studentID: string): Observable<Class[]> {
    const url = this.baseURL + `?sid=${studentID}&mode=register`;

    return this.http
      .get<Class[]>(url)
      .pipe(catchError(this.handleError<Class[]>('getNewClasses', [])));
  }
}
