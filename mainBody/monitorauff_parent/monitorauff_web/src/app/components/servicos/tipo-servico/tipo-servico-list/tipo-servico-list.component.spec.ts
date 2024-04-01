import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TipoServicoListComponent } from './tipo-servico-list.component';

describe('TipoServicoListComponent', () => {
  let component: TipoServicoListComponent;
  let fixture: ComponentFixture<TipoServicoListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TipoServicoListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TipoServicoListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
