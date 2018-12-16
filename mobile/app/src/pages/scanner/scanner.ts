import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, ToastController } from 'ionic-angular';
import { QRScanner, QRScannerStatus } from '@ionic-native/qr-scanner';
import { HttpClient } from '@angular/common/http';

@IonicPage()
@Component({
  selector: 'page-scanner',
  templateUrl: 'scanner.html',
})
export class ScannerPage {

  scanSub: any;

  constructor(
    public navCtrl: NavController,
    private qrScanner: QRScanner,
    public toastCtrl: ToastController,
    private http: HttpClient,
    public navParams: NavParams) {
  }

  ionViewWillEnter() {

    this.qrScanner.prepare()
      .then((status: QRScannerStatus) => {
        if (status.authorized) {
          console.log('Camera Permission Given');
          this.presentToast('Camera Permission Given')

          this.scanSub = this.qrScanner.scan().subscribe((text: string) => {

            this.http.get("http://10.0.30.118:5000/mark_store/" + text).subscribe()

            console.log('Scanned something', text);
            this.presentToast('Scanned' + text)
            this.qrScanner.hide();
            this.scanSub.unsubscribe();

          });

          this.qrScanner.show();

        } else if (status.denied) {
          console.log('Camera permission denied');
          this.presentToast('Camera permission denied')
        } else {
          console.log('Permission denied for this runtime.');
          this.presentToast('Permission denied for this runtime.')
        }
      })
      .catch((e: any) => console.log('Error is', e));

  }

  ionViewWillLeave() {
    this.qrScanner.hide(); // hide camera preview
    this.scanSub.unsubscribe(); // stop scanning
    this.hideCamera();
  }

  showCamera() {
    (window.document.querySelector('ion-app') as HTMLElement).classList.add('cameraView');
  }

  hideCamera() {
    (window.document.querySelector('ion-app') as HTMLElement).classList.remove('cameraView');
  }

  presentToast(msg) {
    const toast = this.toastCtrl.create({
      message: msg,
      duration: 3000
    });
    toast.present();
  }

}
