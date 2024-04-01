import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { MessageService } from 'primeng/api';
import { BaseListComponent } from 'src/app/shared/base/base-list/base-list.component';
import { Monitor } from '../monitor.model';
import { MonitorService } from '../monitor.service';

@Component({
  selector: 'app-monitor-list',
  templateUrl: './monitor-list.component.html',
  styleUrls: ['./monitor-list.component.scss'],
})
export class MonitorListComponent extends BaseListComponent<Monitor> {
  constructor(
    override service: MonitorService,
    router: Router,
    route: ActivatedRoute,
    messageService: MessageService
  ) {
    super(service, router, route, messageService);
  }

  protected afterLoadModel(): void {
    throw new Error('Method not implemented.');
  }
}
