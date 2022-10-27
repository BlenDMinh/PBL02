import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginBoxComponent } from './components/login-box/login-box.component';
import { ProfileComponent } from './components/profile/profile.component';
import { StudentListComponent } from './components/student-list/student-list.component';
import { LoginGuard } from './login.guard';

const routes: Routes = [
  { path: 'main', component: StudentListComponent },
  { path: 'login', component: LoginBoxComponent },
  {
    path: 'profile',
    component: ProfileComponent,
    canActivate: [LoginGuard],
  },
  { path: '', redirectTo: '/main', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
