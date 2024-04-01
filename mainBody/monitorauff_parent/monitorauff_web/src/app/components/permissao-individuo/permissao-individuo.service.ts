import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BaseService } from 'src/app/shared/base/base.service';
import { PermissaoIndividuo } from './permissao-individuo.model';

@Injectable({
  providedIn: 'root',
})
export class PermissaoIndividuoService extends BaseService<PermissaoIndividuo> {
  protected resourceName: string = 'permissao-individuo';

  constructor(http: HttpClient) {
    super(http);
  }
}
