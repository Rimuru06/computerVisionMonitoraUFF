import { query } from '@angular/animations';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { BaseModel } from './base.model';

@Injectable({
  providedIn: 'root',
})
export abstract class BaseService<T extends BaseModel> {
  protected readonly apiUrl: string = 'http://localhost:8000';
  public readonly pathImageFace = `${this.apiUrl}/media/deteccoes/faces`;
  protected abstract resourceName: string;

  constructor(protected http: HttpClient) {}

  protected getResourceName(): string {
    return this.resourceName;
  }

  protected getResourceUrl(): string {
    return `${this.apiUrl}/${this.getResourceName()}`;
  }

  public getAll(queryParams?: any): Observable<T[]> {
    const options = { params: queryParams };
    return this.http.get<T[]>(
      `${this.apiUrl}/${this.getResourceName()}/`,
      options
    );
  }

  public get(id: number): Observable<T> {
    return this.http.get<T>(`${this.apiUrl}/${this.getResourceName()}/${id}/`);
  }
}
