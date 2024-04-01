import { BaseModel } from 'src/app/shared/base/base.model';

export class EtiquetaIndividuo extends BaseModel {
  nome!: string;
  descricao!: string;
  permissoes!: number[];

  constructor() {
    super();
  }
}
