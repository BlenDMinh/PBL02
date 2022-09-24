import { Injectable } from '@angular/core';

import { Observable } from 'rxjs';

import { Student } from './student';

@Injectable({
  providedIn: 'root'
})
export class StudentService {
  
  constructor() { }

  getStudent(): Observable<Student[]> {
    
    return Student;
  }
}
