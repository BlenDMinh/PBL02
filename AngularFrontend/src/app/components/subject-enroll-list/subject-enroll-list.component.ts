import { Component, OnInit } from '@angular/core';
import { SubjectEnrollService } from 'src/app/services/subject-enroll.service';

@Component({
  selector: 'app-subject-enroll-list',
  templateUrl: './subject-enroll-list.component.html',
  styleUrls: ['./subject-enroll-list.component.css']
})
export class SubjectEnrollListComponent implements OnInit {
  testDatas: any;
  currentTestData = null;
  currentIndex = -1;
  title = '';

  constructor(private subjectEnrollService: SubjectEnrollService) { }

  ngOnInit(): void {
    
  }
  retrieveTutorials(): void {
    this.subjectEnrollService.getAll()
      .subscribe(
        data => {
          this.testDatas = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  refreshList(): void {
    this.retrieveTutorials();
    this.currentTestData = null;
    this.currentIndex = -1;
  }

  setActiveTutorial(tutorial:any, index:any): void {
    this.currentTestData = tutorial;
    this.currentIndex = index;
  }

  removeAllTutorials(): void {
    this.subjectEnrollService.deleteAll()
      .subscribe(
        response => {
          console.log(response);
          this.retrieveTutorials();
        },
        error => {
          console.log(error);
        });
  }

  searchTitle(): void {
    this.subjectEnrollService.findByTitle(this.title)
      .subscribe(
        data => {
          this.testDatas = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }
}
