import { TestBed } from '@angular/core/testing';

import { ServicoDeteccaoFaceService } from './servico-deteccao-face.service';

describe('ServicoDeteccaoFaceService', () => {
  let service: ServicoDeteccaoFaceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ServicoDeteccaoFaceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
