import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'berita',
    pathMatch: 'full',
  },
  {
    path: 'berita',
    loadChildren: () =>
      import('./pages/berita/berita.module').then((m) => m.BeritaPageModule),
  },
  {
    path: 'kelola',
    loadChildren: () =>
      import('./pages/kelola/kelola.module').then((m) => m.KelolaPageModule),
  },
  {
    path: 'kencan',
    loadChildren: () =>
      import('./pages/kencan/kencan.module').then((m) => m.KencanPageModule),
  },
  {
    path: 'laporan',
    loadChildren: () =>
      import('./pages/laporan/laporan.module').then((m) => m.LaporanPageModule),
  },
  {
    path: 'user',
    loadChildren: () => import('./pages/user/user.module').then( m => m.UserPageModule)
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules }),
  ],
  exports: [RouterModule],
})
export class AppRoutingModule {}
