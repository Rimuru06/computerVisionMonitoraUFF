import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MessageService } from 'primeng/api';
import { BaseDetailComponent } from 'src/app/shared/base/base-detail/base-detail.component';
import { ServicoDeteccaoFace } from '../servico-deteccao-face.model';
import { ServicoDeteccaoFaceService } from '../servico-deteccao-face.service';

@Component({
  selector: 'app-servico-deteccao-face-detail',
  templateUrl: './servico-deteccao-face-detail.component.html',
  styleUrls: ['./servico-deteccao-face-detail.component.scss'],
})
export class ServicoDeteccaoFaceDetailComponent extends BaseDetailComponent<ServicoDeteccaoFace> {
  public individuo!: ServicoDeteccaoFace;

  constructor(
    override service: ServicoDeteccaoFaceService,
    route: ActivatedRoute,
    messageService: MessageService
  ) {
    super(service, route, messageService);
  }

  protected afterLoadModel(): void {
    throw new Error('Method not implemented.');
  }
}
