import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Class } from '../models/class';

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

  private baseURL = `http://127.0.0.1:8000/api/classsection`;

  getClasses(): Observable<Class[]> {
    return this.http
      .get<Class[]>(this.baseURL)
      .pipe(catchError(this.handleError<Class[]>('getClasses', [])));
  }

  getClass(id: string): Observable<Class> {
    return this.http
      .get<Class>(this.baseURL + `/${id}`)
      .pipe(catchError(this.handleError<Class>('getClasses')));
  }

  getClassesAttendedByStudent(studentID: string): Observable<Class[]> {
    return this.http
      .get<Class[]>(this.baseURL + `?sid=${studentID}`)
      .pipe(
        catchError(this.handleError<Class[]>('getClassesAttendedByStudent', []))
      );
  }

  deleteClass(classID: string, studentID: Number): Observable<any> {
    const options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      }),
      body: {
        sid: JSON.stringify(studentID),
      },
    };

    return this.http.delete(this.baseURL + `/${classID}`, options).pipe();
  }
}
