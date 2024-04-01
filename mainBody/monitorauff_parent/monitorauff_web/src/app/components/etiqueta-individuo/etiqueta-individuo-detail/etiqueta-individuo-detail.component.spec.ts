import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EtiquetaIndividuoDetailComponent } from './etiqueta-individuo-detail.component';

describe('EtiquetaIndividuoDetailComponent', () => {
  let component: EtiquetaIndividuoDetailComponent;
  let fixture: ComponentFixture<EtiquetaIndividuoDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EtiquetaIndividuoDetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EtiquetaIndividuoDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
