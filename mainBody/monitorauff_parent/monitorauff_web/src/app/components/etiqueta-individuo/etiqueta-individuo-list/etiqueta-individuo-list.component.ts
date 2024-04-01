import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { MessageService } from 'primeng/api';
import { BaseListComponent } from 'src/app/shared/base/base-list/base-list.component';
import { EtiquetaIndividuo } from '../etiqueta-individuo.model';
import { EtiquetaIndividuoService } from '../etiqueta-individuo.service';

@Component({
  selector: 'app-etiqueta-individuo-list',
  templateUrl: './etiqueta-individuo-list.component.html',
  styleUrls: ['./etiqueta-individuo-list.component.scss'],
})
export class EtiquetaIndividuoListComponent extends BaseListComponent<EtiquetaIndividuo> {
  constructor(
    service: EtiquetaIndividuoService,
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
