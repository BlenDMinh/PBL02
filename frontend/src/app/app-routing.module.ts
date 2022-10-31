import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ClassSignComponent } from './components/class-sign/class-sign.component';
import { LoginBoxComponent } from './components/login-box/login-box.component';
import { ProfileComponent } from './components/profile/profile.component';
import { StudentListComponent } from './components/student-list/student-list.component';
import { TimetableComponent } from './components/timetable/timetable.component';

const routes: Routes = [
  { path: 'main', component: StudentListComponent },
  { path: 'login', component: LoginBoxComponent },
  { path: 'profile', component: ProfileComponent },
  { path: 'classSign', component: ClassSignComponent },
  { path: 'timetable', component: TimetableComponent },
  { path: '', redirectTo: '/main', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
