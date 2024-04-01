import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MessageService } from 'primeng/api';
import { BaseDetailComponent } from 'src/app/shared/base/base-detail/base-detail.component';
import { Group } from '../group.model';
import { GroupService } from '../group.service';

@Component({
  selector: 'app-group-detail',
  templateUrl: './group-detail.component.html',
  styleUrls: ['./group-detail.component.scss'],
})
export class GroupDetailComponent extends BaseDetailComponent<Group> {
  constructor(
    override service: GroupService,
    route: ActivatedRoute,
    messageService: MessageService
  ) {
    super(service, route, messageService);
  }

  protected afterLoadModel(): void {
    throw new Error('Method not implemented.');
  }
}
