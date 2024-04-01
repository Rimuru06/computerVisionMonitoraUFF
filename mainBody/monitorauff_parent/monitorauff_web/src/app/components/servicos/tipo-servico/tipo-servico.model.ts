import { BaseModel } from 'src/app/shared/base/base.model';

export class TipoServico extends BaseModel {
  nome!: string;
  descricao!: string;

  constructor() {
    super();
  }
}
