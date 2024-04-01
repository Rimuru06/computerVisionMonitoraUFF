import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { MessageService } from 'primeng/api';
import { BaseListComponent } from 'src/app/shared/base/base-list/base-list.component';
import { Group } from '../group.model';
import { GroupService } from '../group.service';

@Component({
  selector: 'app-group-list',
  templateUrl: './group-list.component.html',
  styleUrls: ['./group-list.component.scss'],
})
export class GroupListComponent extends BaseListComponent<Group> {
  constructor(
    override service: GroupService,
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
