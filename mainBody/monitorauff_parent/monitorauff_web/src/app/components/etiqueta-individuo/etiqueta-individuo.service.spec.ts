import { TestBed } from '@angular/core/testing';

import { EtiquetaIndividuoService } from './etiqueta-individuo.service';

describe('EtiquetaIndividuoService', () => {
  let service: EtiquetaIndividuoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EtiquetaIndividuoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
