import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EtiquetaIndividuoListComponent } from './etiqueta-individuo-list.component';

describe('EtiquetaIndividuoListComponent', () => {
  let component: EtiquetaIndividuoListComponent;
  let fixture: ComponentFixture<EtiquetaIndividuoListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EtiquetaIndividuoListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EtiquetaIndividuoListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
