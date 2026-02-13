import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

export type ItemStatus = 'verfuegbar' | 'reserviert' | 'verkauft';

export interface ItemRead {
  id: number;
  title: string;
  description: string;
  price: number | null;
  status: ItemStatus;
  created_at: string;
  updated_at: string | null;
  category_id: number;
}

@Injectable({ providedIn: 'root' })
export class ItemsService {
  private baseUrl = `${environment.apiUrl}/items`;

  constructor(private http: HttpClient) {}

  list(status?: ItemStatus, categoryId?: number): Observable<ItemRead[]> {
    const params: any = {};
    if (status) params.status = status;
    if (categoryId) params.category_id = categoryId;
    return this.http.get<ItemRead[]>(this.baseUrl, { params });
  }
}

