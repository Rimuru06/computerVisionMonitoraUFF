import { Component, ViewChild } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { MessageService } from 'primeng/api';
import { FileUpload } from 'primeng/fileupload';
import { BaseListComponent } from 'src/app/shared/base/base-list/base-list.component';
import { Individuo } from '../../individuo/individuo.model';
import { IndividuoService } from '../../individuo/individuo.service';
import { OcorrenciaFace } from '../ocorrencia-face.model';
import { OcorrenciaFaceService } from '../ocorrencia-face.service';

@Component({
  selector: 'app-ocorrencia-face-list',
  templateUrl: './ocorrencia-face-list.component.html',
  styleUrls: ['./ocorrencia-face-list.component.scss'],
})
export class OcorrenciaFaceListComponent extends BaseListComponent<OcorrenciaFace> {
  @ViewChild('fileUploader') fileUploader!: FileUpload;

  public individuos: Individuo[] = [];
  public filtered: boolean = false;

  constructor(
    override service: OcorrenciaFaceService,
    router: Router,
    route: ActivatedRoute,
    messageService: MessageService,
    private individuoService: IndividuoService
  ) {
    super(service, router, route, messageService);
  }

  protected afterLoadModel(): void {
    this.modelList.forEach((face) => {
      if (!face.individuo) return;

      this.individuoService.get(face.individuo).subscribe({
        next: (response) => {
          if (!this.individuos.some((i) => i.id === face.individuo)) {
            this.individuos.push(response);
          }
        },
        error: (error: any) => {
          let msg = `Não foi possível carregar o indivíduo de ID ${face.individuo}`;
          this.showErrorMessage();
        },
      });
    });
  }

  public onFiltering($event: any): void {
    this.service.filterByImage($event.files[0]).subscribe({
      next: (response: OcorrenciaFace[]) => {
        this.modelList = response;
        this.filtered = true;
        this.fileUploader.clear();
        this.afterLoadModel();
      },
      error: (error: any) => {
        console.error(error);
        this.showErrorMessage();
      },
    });
  }

  public clearFilter(): void {
    this.loadModelList();
    this.filtered = false;
  }

  public getIndividuo(id: number): Individuo | null {
    if (!id) return null;

    let individuo = this.individuos.find((i) => i.id === id);

    return individuo || null;
  }

  public getNameWithoutExtension(fileName: string): string {
    return fileName.substring(0, fileName.lastIndexOf('.'));
  }

  public getImageUrl(face: OcorrenciaFace): string {
    return `${this.service.pathImageFace}/${face?.img_filename || 'default'}`;
  }

  public getUploadUrl(): string {
    return this.service.pathUploadFace;
  }
}
