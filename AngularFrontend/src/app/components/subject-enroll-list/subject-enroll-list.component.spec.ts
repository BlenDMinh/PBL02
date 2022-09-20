import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SubjectEnrollListComponent } from './subject-enroll-list.component';

describe('SubjectEnrollListComponent', () => {
  let component: SubjectEnrollListComponent;
  let fixture: ComponentFixture<SubjectEnrollListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SubjectEnrollListComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SubjectEnrollListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
