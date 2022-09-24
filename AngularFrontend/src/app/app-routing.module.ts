import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SubjectEnrollListComponent } from './components/subject-enroll-list/subject-enroll-list.component';
import { SubjectEnrollDetailsComponent } from './components/subject-enroll-details/subject-enroll-details.component';
import { AddSubjectEnrollComponent } from './components/add-subject-enroll/add-subject-enroll.component';
import { StudentComponent } from './student/student.component';

const routes: Routes = [
  // { path: '', redirectTo: 'SubjectEnroll', pathMatch: 'full' },
  // { path: 'SubjectEnroll', component: SubjectEnrollListComponent },
  // { path: 'SubjectEnroll/:id', component: SubjectEnrollDetailsComponent },
  // { path: 'add', component: AddSubjectEnrollComponent },
  { path: '', component: StudentComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
