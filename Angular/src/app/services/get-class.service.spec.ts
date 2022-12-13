import { TestBed } from '@angular/core/testing';

import { GetClassService } from './get-class.service';

describe('GetClassService', () => {
  let service: GetClassService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GetClassService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
