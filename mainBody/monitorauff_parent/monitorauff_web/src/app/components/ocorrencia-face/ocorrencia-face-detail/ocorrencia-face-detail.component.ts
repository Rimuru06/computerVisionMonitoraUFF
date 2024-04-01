import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { MessageService } from 'primeng/api';

import { BaseDetailComponent } from 'src/app/shared/base/base-detail/base-detail.component';
import { Individuo } from '../../individuo/individuo.model';
import { IndividuoService } from '../../individuo/individuo.service';
import { OcorrenciaFace } from '../ocorrencia-face.model';
import { OcorrenciaFaceService } from '../ocorrencia-face.service';

@Component({
  selector: 'app-ocorrencia-face-detail',
  templateUrl: './ocorrencia-face-detail.component.html',
  styleUrls: ['./ocorrencia-face-detail.component.scss'],
})
export class OcorrenciaFaceDetailComponent extends BaseDetailComponent<OcorrenciaFace> {
  public individuo!: Individuo | null;
  public individuoOptions: Individuo[] = [];
  public selectedIndividuo!: Individuo;

  constructor(
    override service: OcorrenciaFaceService,
    route: ActivatedRoute,
    messageService: MessageService,
    private individuoService: IndividuoService
  ) {
    super(service, route, messageService);
  }

  override ngOnInit(): void {
    super.ngOnInit();
    this.loadOptions();
  }

  protected afterLoadModel(): void {
    if (this.model.individuo) {
      this.individuoService.get(this.model.individuo).subscribe({
        next: (response: Individuo) => {
          this.individuo = response;
        },
        error: (error: any) => {
          console.error(error);
          this.showErrorMessage();
        },
      });
    }
  }

  private loadOptions(): void {
    this.individuoService.getAll().subscribe({
      next: (response: Individuo[]) => {
        this.individuoOptions = response;
      },
      error: (error: any) => {
        console.error(error);
        this.showErrorMessage('Erro ao carregar lista de indivíduos.');
      },
    });
  }

  public objectToString(object: any): string {
    return JSON.stringify(object);
  }

  public getNameWithoutExtension(fileName: string): string {
    return fileName?.substring(0, fileName.lastIndexOf('.')) || '';
  }

  public getImageUrl(): string {
    return `${this.service.pathImageFace}/${
      this.model?.img_filename || 'default'
    }`;
  }

  public associarIndividuo(): void {
    this.service
      .associarIndividuo(this.model.id, this.selectedIndividuo.id)
      .subscribe({
        next: () => {
          this.loadModel(this.model.id);
        },
        error: (error: any) => {
          console.error(error);
          this.showErrorMessage('Erro ao associar individuo.');
        },
      });
  }

  public desassociarIndividuo(): void {
    this.service.desassociarIndividuo(this.model.id).subscribe({
      next: () => {
        this.individuo = null;
        this.loadModel(this.model.id);
      },
      error: (error: any) => {
        console.error(error);
        this.showErrorMessage('Erro ao desassociar individuo.');
      },
    });
  }
}
