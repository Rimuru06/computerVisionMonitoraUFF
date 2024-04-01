import { BaseModel } from 'src/app/shared/base/base.model';

export class PermissaoIndividuo extends BaseModel {
  nome!: string;
  descricao!: string;

  constructor() {
    super();
  }
}
