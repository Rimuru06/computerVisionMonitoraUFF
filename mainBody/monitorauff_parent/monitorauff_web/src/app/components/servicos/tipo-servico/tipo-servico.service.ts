import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { BaseService } from 'src/app/shared/base/base.service';
import { TipoServico } from './tipo-servico.model';

@Injectable({
  providedIn: 'root',
})
export class TipoServicoService extends BaseService<TipoServico> {
  protected resourceName: string = 'tipo-servico';

  constructor(http: HttpClient) {
    super(http);
  }

  public getByMonitorId(monitorId: number): Observable<TipoServico[]> {
    return this.http.get<TipoServico[]>(
      `${this.getResourceUrl()}/by-monitor/`,
      { params: { monitor_id: monitorId } }
    );
  }

  public vincularMonitor(
    tipoServicoId: number,
    monitoresIds: number[]
  ): Observable<any> {
    return this.http.post<any>(
      `${this.getResourceUrl()}/${tipoServicoId}/vinculo-monitor/`,
      { monitores: monitoresIds }
    );
  }

  public desvincularMonitor(
    tipoServicoId: number,
    monitoresIds: number[]
  ): Observable<any> {
    return this.http.delete<any>(
      `${this.getResourceUrl()}/${tipoServicoId}/vinculo-monitor/`,
      { body: { monitores: monitoresIds } }
    );
  }
}
