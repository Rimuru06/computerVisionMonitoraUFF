import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IndividuoDetailComponent } from './individuo-detail.component';

describe('IndividuoDetailComponent', () => {
  let component: IndividuoDetailComponent;
  let fixture: ComponentFixture<IndividuoDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ IndividuoDetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(IndividuoDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
