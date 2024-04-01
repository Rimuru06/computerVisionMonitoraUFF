import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { BaseService } from 'src/app/shared/base/base.service';
import { Individuo } from './individuo.model';

@Injectable({
  providedIn: 'root',
})
export class IndividuoService extends BaseService<Individuo> {
  protected resourceName: string = 'individuo';
  public readonly pathUploadFace = `${this.apiUrl}/${this.resourceName}/by-image/`;

  constructor(http: HttpClient) {
    super(http);
  }

  public findByFaceId(faceId: number): Observable<Individuo> {
    return this.http.get<Individuo>(`${this.getResourceUrl()}/by-face-id`, {
      params: { face_id: faceId },
    });
  }

  public filterByImage(image: any): Observable<Individuo[]> {
    const form = new FormData();
    form.append('file', image);
    return this.http.post<Individuo[]>(`${this.pathUploadFace}`, form);
  }

  public addEtiquetas(
    individuoId: number,
    etiquetas: number[]
  ): Observable<Individuo> {
    return this.http.post<Individuo>(
      `${this.getResourceUrl()}/${individuoId}/etiqueta/`,
      {
        etiquetas,
      }
    );
  }

  public removeEtiquetas(
    individuoId: number,
    etiquetas: number[]
  ): Observable<Individuo> {
    return this.http.delete<Individuo>(
      `${this.getResourceUrl()}/${individuoId}/etiqueta/`,
      {
        body: { etiquetas },
      }
    );
  }
}
