import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NavbarComponent } from './components/navbar/navbar.component';
import { StudentTableComponent } from './components/student-table/student-table.component';
import { StudentListComponent } from './components/student-list/student-list.component';
import { LoginBoxComponent } from './components/login-box/login-box.component';

@NgModule({
  declarations: [
    AppComponent,
    StudentTableComponent,
    StudentListComponent,
    LoginBoxComponent,
    NavbarComponent,
  ],
  imports: [BrowserModule, AppRoutingModule, NgbModule, HttpClientModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
