import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { BaseService } from 'src/app/shared/base/base.service';
import { Group } from './group.model';

@Injectable({
  providedIn: 'root',
})
export class GroupService extends BaseService<Group> {
  protected resourceName: string = 'grupo';

  constructor(http: HttpClient) {
    super(http);
  }

  public getByMonitorId(monitorId: number): Observable<Group[]> {
    const options = { params: { monitor_id: monitorId } };
    return this.http.get<Group[]>(
      `${this.apiUrl}/${this.getResourceName()}/by-monitor`,
      options
    );
  }
}
