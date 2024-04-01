import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MessageService } from 'primeng/api';
import { BaseDetailComponent } from 'src/app/shared/base/base-detail/base-detail.component';
import { TipoServico } from '../tipo-servico.model';
import { TipoServicoService } from '../tipo-servico.service';

@Component({
  selector: 'app-tipo-servico-detail',
  templateUrl: './tipo-servico-detail.component.html',
  styleUrls: ['./tipo-servico-detail.component.scss'],
})
export class TipoServicoDetailComponent extends BaseDetailComponent<TipoServico> {
  public individuo!: TipoServico;

  constructor(
    override service: TipoServicoService,
    route: ActivatedRoute,
    messageService: MessageService
  ) {
    super(service, route, messageService);
  }

  protected afterLoadModel(): void {
    throw new Error('Method not implemented.');
  }
}
