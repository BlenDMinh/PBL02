import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SubjectEnrollDetailsComponent } from './subject-enroll-details.component';

describe('SubjectEnrollDetailsComponent', () => {
  let component: SubjectEnrollDetailsComponent;
  let fixture: ComponentFixture<SubjectEnrollDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SubjectEnrollDetailsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SubjectEnrollDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
