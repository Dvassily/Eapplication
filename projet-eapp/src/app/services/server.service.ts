import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";


@Injectable()
export class ServerService {
  constructor(private httpClient: HttpClient) {
  }

  getResult(query) {
    return this.httpClient.get(`http://localhost:5000/get/${query}`)
  }

  parseRequest(query) {
    return this.httpClient.get(`http://localhost:5000/parse_query/${query}`)
  }
}
