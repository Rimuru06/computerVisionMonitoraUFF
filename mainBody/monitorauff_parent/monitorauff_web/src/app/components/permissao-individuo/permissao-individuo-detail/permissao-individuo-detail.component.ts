import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MessageService } from 'primeng/api';
import { BaseDetailComponent } from 'src/app/shared/base/base-detail/base-detail.component';
import { PermissaoIndividuo } from '../permissao-individuo.model';
import { PermissaoIndividuoService } from '../permissao-individuo.service';

@Component({
  selector: 'app-permissao-individuo-detail',
  templateUrl: './permissao-individuo-detail.component.html',
  styleUrls: ['./permissao-individuo-detail.component.scss'],
})
export class PermissaoIndividuoDetailComponent extends BaseDetailComponent<PermissaoIndividuo> {
  public default!: PermissaoIndividuo;

  constructor(
    service: PermissaoIndividuoService,
    route: ActivatedRoute,
    messageService: MessageService
  ) {
    super(service, route, messageService);
  }

  protected afterLoadModel(): void {
    throw new Error('Method not implemented.');
  }
}
