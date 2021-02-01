import {Component} from '@angular/core';
import {ServerService} from "./services/server.service";
import {NgxSpinnerService} from "ngx-spinner";
import { MatSlideToggleChange } from '@angular/material/slide-toggle';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'projet-eapp';
  res = null;
  startTime = null;
  endTime = null;

  public noCache = false;


  constructor(private serverService: ServerService,
              private spinner: NgxSpinnerService) {

  }

  getTime(){
    var time = new Date().getTime();
    return time 
  }
  

  onSearch(query: any) {
    this.spinner.show();

    this.serverService.getResult(query, this.noCache).subscribe(res => {
      this.res = res;
      this.spinner.hide()
      this.end();
    })
    console.log(this.startTime, this.endTime);

  }
  begin(){  
    this.startTime = new Date().getTime();
  }
  end(){
    this.endTime = new Date().getTime();
  }
  duration(){
    return this.endTime - this.startTime;
  }

}