import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { BaseService } from 'src/app/shared/base/base.service';
import { OcorrenciaFace } from './ocorrencia-face.model';

@Injectable({
  providedIn: 'root',
})
export class OcorrenciaFaceService extends BaseService<OcorrenciaFace> {
  protected resourceName: string = 'ocorrencia-face';
  public readonly pathUploadFace = `${this.apiUrl}/${this.resourceName}/filter-by-image/`;

  constructor(http: HttpClient) {
    super(http);
  }

  public filterByImage(image: any): Observable<OcorrenciaFace[]> {
    const form = new FormData();
    form.append('file', image);
    return this.http.post<OcorrenciaFace[]>(`${this.pathUploadFace}`, form);
  }

  public filterByIndividuoId(individuo: number): Observable<OcorrenciaFace[]> {
    return this.getAll({ individuo });
  }

  public associarIndividuo(id: number, individuoId: number): Observable<any> {
    return this.http.post<any>(
      `${this.apiUrl}/${this.resourceName}/${id}/associar-individuo/`,
      { individuo: individuoId }
    );
  }

  public desassociarIndividuo(id: number): Observable<any> {
    return this.http.post<any>(
      `${this.apiUrl}/${this.resourceName}/${id}/desassociar-individuo/`,
      {}
    );
  }
}
