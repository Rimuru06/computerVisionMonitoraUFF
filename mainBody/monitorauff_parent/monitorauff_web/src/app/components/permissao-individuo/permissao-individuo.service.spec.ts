import { TestBed } from '@angular/core/testing';

import { PermissaoIndividuoService } from './permissao-individuo.service';

describe('PermissaoIndividuoService', () => {
  let service: PermissaoIndividuoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PermissaoIndividuoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
