import { TestBed } from '@angular/core/testing';

import { IndividuoService } from './individuo.service';

describe('IndividuoService', () => {
  let service: IndividuoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(IndividuoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
