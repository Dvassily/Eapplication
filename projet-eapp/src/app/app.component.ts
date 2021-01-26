import { Component } from '@angular/core';
import {ServerService} from "./services/server.service";
import {NgxSpinnerService} from "ngx-spinner";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'projet-eapp';
  res = null;

  constructor(private serverService: ServerService,
              private spinner: NgxSpinnerService) {

  }


  handleQuery(query : any) {
    this.spinner.show()
    this.serverService.getResult(query).subscribe(res => {
      this.res = res;
      this.spinner.hide()
    })
  }
}
