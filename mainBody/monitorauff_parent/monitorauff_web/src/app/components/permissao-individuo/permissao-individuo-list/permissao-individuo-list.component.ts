import { Component } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { MessageService } from 'primeng/api';
import { BaseListComponent } from 'src/app/shared/base/base-list/base-list.component';
import { PermissaoIndividuo } from '../permissao-individuo.model';
import { PermissaoIndividuoService } from '../permissao-individuo.service';

@Component({
  selector: 'app-permissao-individuo-list',
  templateUrl: './permissao-individuo-list.component.html',
  styleUrls: ['./permissao-individuo-list.component.scss'],
})
export class PermissaoIndividuoListComponent extends BaseListComponent<PermissaoIndividuo> {
  constructor(
    service: PermissaoIndividuoService,
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
