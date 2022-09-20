import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AddSubjectEnrollComponent } from './components/add-subject-enroll/add-subject-enroll.component';
import { SubjectEnrollDetailsComponent } from './components/subject-enroll-details/subject-enroll-details.component';
import { SubjectEnrollListComponent } from './components/subject-enroll-list/subject-enroll-list.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    AddSubjectEnrollComponent,
    SubjectEnrollDetailsComponent,
    SubjectEnrollListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
