import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TipoServicoDetailComponent } from './tipo-servico-detail.component';

describe('TipoServicoDetailComponent', () => {
  let component: TipoServicoDetailComponent;
  let fixture: ComponentFixture<TipoServicoDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TipoServicoDetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TipoServicoDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
