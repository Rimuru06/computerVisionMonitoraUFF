import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MessageService } from 'primeng/api';
import { BaseDetailComponent } from 'src/app/shared/base/base-detail/base-detail.component';
import { EtiquetaIndividuo } from '../../etiqueta-individuo/etiqueta-individuo.model';
import { EtiquetaIndividuoService } from '../../etiqueta-individuo/etiqueta-individuo.service';
import { OcorrenciaFace } from '../../ocorrencia-face/ocorrencia-face.model';
import { OcorrenciaFaceService } from '../../ocorrencia-face/ocorrencia-face.service';
import { Individuo } from '../individuo.model';
import { IndividuoService } from '../individuo.service';

@Component({
  selector: 'app-individuo-detail',
  templateUrl: './individuo-detail.component.html',
  styleUrls: ['./individuo-detail.component.scss'],
})
export class IndividuoDetailComponent extends BaseDetailComponent<Individuo> {
  public faces: OcorrenciaFace[] = [];
  public etiquetas: EtiquetaIndividuo[] = [];
  public etiquetaOptions: EtiquetaIndividuo[] = [];
  public selectedEtiquetas!: number[];

  constructor(
    override service: IndividuoService,
    route: ActivatedRoute,
    messageService: MessageService,
    private ocorrenciaService: OcorrenciaFaceService,
    private etiquetaService: EtiquetaIndividuoService
  ) {
    super(service, route, messageService);
  }

  override ngOnInit(): void {
    super.ngOnInit();
    this.loadOptions();
  }

  protected afterLoadModel(): void {
    this.faces = [];
    this.etiquetas = [];

    this.ocorrenciaService.filterByIndividuoId(this.model.id).subscribe({
      next: (response: OcorrenciaFace[]) => {
        this.faces = response;
      },
      error: (error: any) => {
        let msg = `Não foi possível carregar as faces`;
        this.showErrorMessage(msg);
      },
    });

    this.model.etiquetas.forEach((etiquetaId) => {
      this.etiquetaService.get(etiquetaId).subscribe({
        next: (response) => {
          this.etiquetas.push(response);
        },
        error: (error: any) => {
          let msg = `Não foi possível carregar a etiqueta de ID ${etiquetaId}`;
          this.showErrorMessage(msg);
        },
      });
    });
  }

  private loadOptions(): void {
    this.etiquetaService.getAll().subscribe({
      next: (response: EtiquetaIndividuo[]) => {
        this.etiquetaOptions = response;
      },
      error: (error: any) => {
        console.error(error);
        this.showErrorMessage('Erro ao carregar lista de indivíduos.');
      },
    });
  }

  public getIndividuoImageUrl(): string {
    let face = new OcorrenciaFace();

    if (this.faces.length) face = this.faces[0];

    return this.getImageUrl(face);
  }

  public getImageUrl(face: OcorrenciaFace): string {
    return `${this.service.pathImageFace}/${face?.img_filename || 'default'}`;
  }

  public getNameWithoutExtension(fileName: string): string {
    return fileName.substring(0, fileName.lastIndexOf('.'));
  }

  public desassociarFace(face: OcorrenciaFace): void {
    this.ocorrenciaService.desassociarIndividuo(face.id).subscribe({
      next: () => {
        this.showSucessMessage();
        this.loadModel(this.model.id);
      },
      error: (error: any) => {
        console.error(error);
        this.showErrorMessage('Erro ao desassociar face.');
      },
    });
  }

  public atribuirEtiquetas(): void {
    this.service.addEtiquetas(this.model.id, this.selectedEtiquetas).subscribe({
      next: () => {
        this.showSucessMessage();
        this.loadModel(this.model.id);
        this.selectedEtiquetas = [];
      },
      error: () => {
        this.showErrorMessage('Não foi possível realizar a operação.');
      },
    });
  }

  public removerEtiqueta(etiquetaId: number): void {
    this.service.removeEtiquetas(this.model.id, [etiquetaId]).subscribe({
      next: () => {
        this.showSucessMessage();
        this.loadModel(this.model.id);
      },
      error: () => {
        this.showErrorMessage('Não foi possível realizar a operação.');
      },
    });
  }
}
