import { BaseModel } from 'src/app/shared/base/base.model';

export class Individuo extends BaseModel {
  public nome!: string;
  public etiquetas!: number[];

  constructor() {
    super();
  }
}
