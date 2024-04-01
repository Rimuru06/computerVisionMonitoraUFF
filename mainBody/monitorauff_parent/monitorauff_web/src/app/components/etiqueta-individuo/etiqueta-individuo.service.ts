import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BaseService } from 'src/app/shared/base/base.service';
import { EtiquetaIndividuo } from './etiqueta-individuo.model';

@Injectable({
  providedIn: 'root',
})
export class EtiquetaIndividuoService extends BaseService<EtiquetaIndividuo> {
  protected resourceName: string = 'etiqueta-individuo';

  constructor(http: HttpClient) {
    super(http);
  }
}
