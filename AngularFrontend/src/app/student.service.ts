import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Student } from './student';

const baseurl = 'http://localhost:8000/api/StudentManager';
@Injectable({
  providedIn: 'root',
})
export class StudentService {
  constructor(private http: HttpClient) {}

  getAllStudents(): Observable<any> {
    const response = this.http.get(`${baseurl}`);
    return response;
  }

  getStudent(id: any): Observable<any> {
    return this.http.get(`${baseurl}/${id}`);
  }
}
