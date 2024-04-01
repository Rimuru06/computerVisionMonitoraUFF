import { TestBed } from '@angular/core/testing';

import { OcorrenciaFaceService } from './ocorrencia-face.service';

describe('OcorrenciaFaceService', () => {
  let service: OcorrenciaFaceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(OcorrenciaFaceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
