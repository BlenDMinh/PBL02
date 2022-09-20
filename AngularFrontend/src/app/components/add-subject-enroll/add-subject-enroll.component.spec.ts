import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddSubjectEnrollComponent } from './add-subject-enroll.component';

describe('AddSubjectEnrollComponent', () => {
  let component: AddSubjectEnrollComponent;
  let fixture: ComponentFixture<AddSubjectEnrollComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddSubjectEnrollComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddSubjectEnrollComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
