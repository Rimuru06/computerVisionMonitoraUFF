import { BaseModel } from 'src/app/shared/base/base.model';

export class ServicoDeteccaoFace extends BaseModel {
  monitor!: number;
  isActive!: boolean;

  constructor() {
    super();
  }
}
