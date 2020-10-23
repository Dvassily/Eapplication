import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";


@Injectable()
export class ServerService {


  constructor(private httpClient: HttpClient) {
  }

  getWord(word) {
    return this.httpClient.get(`http://localhost:5000/query/${word}`)
  }
}
