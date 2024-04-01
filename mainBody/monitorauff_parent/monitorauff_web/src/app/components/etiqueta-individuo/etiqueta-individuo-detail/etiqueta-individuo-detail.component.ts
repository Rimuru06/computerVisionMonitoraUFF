import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MessageService } from 'primeng/api';
import { BaseDetailComponent } from 'src/app/shared/base/base-detail/base-detail.component';
import { EtiquetaIndividuo } from '../etiqueta-individuo.model';
import { EtiquetaIndividuoService } from '../etiqueta-individuo.service';

@Component({
  selector: 'app-etiqueta-individuo-detail',
  templateUrl: './etiqueta-individuo-detail.component.html',
  styleUrls: ['./etiqueta-individuo-detail.component.scss'],
})
export class EtiquetaIndividuoDetailComponent extends BaseDetailComponent<EtiquetaIndividuo> {
  public individuo!: EtiquetaIndividuo;

  constructor(
    service: EtiquetaIndividuoService,
    route: ActivatedRoute,
    messageService: MessageService
  ) {
    super(service, route, messageService);
  }

  protected afterLoadModel(): void {
    throw new Error('Method not implemented.');
  }
}
