import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class APIService {
  private apiUrl = 'http://localhost:5000/';
  
  constructor(private http : HttpClient) {
    // Does nothing on construction
  }

  submitQuery(query : string) : Observable<any> {
    return this.http.get(this.apiUrl + "/query/" + query);
  }
}
