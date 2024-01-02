import { TestBed } from '@angular/core/testing';

import { NombreDBService } from './nombre-db.service';

describe('NombreDBService', () => {
  let service: NombreDBService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(NombreDBService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
