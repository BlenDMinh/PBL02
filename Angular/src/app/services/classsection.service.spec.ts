import { TestBed } from '@angular/core/testing';

import { ClasssectionService } from './classsection.service';

describe('ClasssectionService', () => {
  let service: ClasssectionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ClasssectionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
