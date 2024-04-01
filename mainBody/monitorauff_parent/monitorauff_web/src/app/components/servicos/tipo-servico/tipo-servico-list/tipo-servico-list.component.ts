import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { MessageService } from 'primeng/api';
import { BaseListComponent } from 'src/app/shared/base/base-list/base-list.component';
import { TipoServico } from '../tipo-servico.model';
import { TipoServicoService } from '../tipo-servico.service';

@Component({
  selector: 'app-tipo-servico-list',
  templateUrl: './tipo-servico-list.component.html',
  styleUrls: ['./tipo-servico-list.component.scss'],
})
export class TipoServicoListComponent extends BaseListComponent<TipoServico> {
  constructor(
    service: TipoServicoService,
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
