import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BaseService } from 'src/app/shared/base/base.service';
import { Monitor } from './monitor.model';

@Injectable({
  providedIn: 'root',
})
export class MonitorService extends BaseService<Monitor> {
  protected resourceName: string = 'monitor';

  constructor(http: HttpClient) {
    super(http);
  }
}
