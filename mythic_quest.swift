/*   Mythic Quest  -  s01e03 15:04

     Source:
      - https://github.com/iaaqibhussain/Camera-with-AVFoundation/blob/master/Camera%20with%20AVFoundation/CameraViewController.swift
*/
    {
    
        let alert = UIAlertController(title: title, message: message, preferredStyle: .Alert)
        let done = UIAlertAction(title: "OK", style: .Default, handler: nil)
        alert.addAction(done)
        self.presentViewController(alert, animated: false, completion: nil)
    }
}

import UIKit
import AVFoundation
import Photos

override func didReceiveMemoryWarning() {
  super.didReceiveMemoryWarning()
}
    
//MARK: - Camera Initialization functions
func initiatePictureCamera(){
print("Picture Camera is Running")
session = AVCaptureSession()
session!.sessionPreset = AVCaptureSessionPresetPhoto
var input : AVCaptureDeviceInput?
var error: NSError?
