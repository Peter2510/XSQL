import { TestBed } from '@angular/core/testing';

import { CompilacionService } from './compilacion.service';

describe('CompilacionService', () => {
  let service: CompilacionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CompilacionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
