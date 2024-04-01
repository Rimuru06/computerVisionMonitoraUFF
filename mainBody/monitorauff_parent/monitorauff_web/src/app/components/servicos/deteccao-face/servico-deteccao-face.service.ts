import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { BaseService } from 'src/app/shared/base/base.service';
import { ServicoDeteccaoFace } from './servico-deteccao-face.model';

@Injectable({
  providedIn: 'root',
})
export class ServicoDeteccaoFaceService extends BaseService<ServicoDeteccaoFace> {
  protected resourceName: string = 'servico_deteccao_face';

  constructor(http: HttpClient) {
    super(http);
  }

  public ativarServico(monitorId: number): Observable<any> {
    return this.http.post<any>(`${this.getResourceUrl()}/ativar/`, {
      monitor: monitorId,
    });
  }

  public desativarServico(monitorId: number): Observable<any> {
    return this.http.post<any>(`${this.getResourceUrl()}/desativar/`, {
      monitor: monitorId,
    });
  }
}
