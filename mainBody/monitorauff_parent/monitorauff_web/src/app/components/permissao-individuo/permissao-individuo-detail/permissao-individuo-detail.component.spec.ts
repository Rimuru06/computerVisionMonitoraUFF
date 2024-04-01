import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PermissaoIndividuoDetailComponent } from './permissao-individuo-detail.component';

describe('PermissaoIndividuoDetailComponent', () => {
  let component: PermissaoIndividuoDetailComponent;
  let fixture: ComponentFixture<PermissaoIndividuoDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PermissaoIndividuoDetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PermissaoIndividuoDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
