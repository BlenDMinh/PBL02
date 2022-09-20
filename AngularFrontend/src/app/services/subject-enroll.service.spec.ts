import { TestBed } from '@angular/core/testing';

import { SubjectEnrollService } from './subject-enroll.service';

describe('SubjectEnrollService', () => {
  let service: SubjectEnrollService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SubjectEnrollService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
