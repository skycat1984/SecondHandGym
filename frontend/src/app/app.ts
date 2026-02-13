import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ItemsService, ItemRead } from './services/items';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './app.html',
})
export class App implements OnInit {
  items: ItemRead[] = [];

  constructor(
    private itemsService: ItemsService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.itemsService.list('verfuegbar').subscribe({
      next: (items) => {
        this.items = items;
        this.cdr.detectChanges(); // <- erzwingt UI-Update
      },
      error: (err) => console.error('API error', err),
    });
  }
}

