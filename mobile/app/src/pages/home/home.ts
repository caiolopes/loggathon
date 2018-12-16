import { Component, OnInit } from '@angular/core';
import { NavController, ToastController } from 'ionic-angular';
import { RoutingProvider } from '../../providers/routing/routing';
import { QRScanner, QRScannerStatus } from '@ionic-native/qr-scanner';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage implements OnInit {

  rota: any = [];

  constructor(
    public navCtrl: NavController,
    private routingProvider: RoutingProvider,
    private qrScanner: QRScanner
  ) {
    this.routingProvider.getRoute().subscribe((res: any) => {
      this.rota = res;
      console.log(this.rota)
    })
  }

  ngOnInit(): void {

  }

  openPage(sells) {
    this.navCtrl.push('ItemsPage', sells)
  }

  openQRScanner() {
    this.navCtrl.push('ScannerPage')
  }

}
