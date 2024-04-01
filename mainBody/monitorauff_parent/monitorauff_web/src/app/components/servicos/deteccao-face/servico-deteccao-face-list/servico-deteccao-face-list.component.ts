import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { MessageService } from 'primeng/api';
import { BaseListComponent } from 'src/app/shared/base/base-list/base-list.component';
import { ServicoDeteccaoFace } from '../servico-deteccao-face.model';
import { ServicoDeteccaoFaceService } from '../servico-deteccao-face.service';

@Component({
  selector: 'app-servico-deteccao-face-list',
  templateUrl: './servico-deteccao-face-list.component.html',
  styleUrls: ['./servico-deteccao-face-list.component.scss'],
})
export class ServicoDeteccaoFaceListComponent extends BaseListComponent<ServicoDeteccaoFace> {
  constructor(
    service: ServicoDeteccaoFaceService,
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
