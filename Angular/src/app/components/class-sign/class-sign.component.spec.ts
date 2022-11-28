import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClassSignComponent } from './class-sign.component';

describe('ClassSignComponent', () => {
  let component: ClassSignComponent;
  let fixture: ComponentFixture<ClassSignComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ClassSignComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ClassSignComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
