import AVFoundation
import Combine
import HaishinKit

final class RTMPPublisher: NSObject, ObservableObject {
    enum ConnectionStatus: String {
        case idle
        case connecting
        case connected
        case publishing
        case stopped
        case failed
    }

    @Published private(set) var status: ConnectionStatus = .idle
    @Published private(set) var lastError: String?

    private let connection = RTMPConnection()
    private let stream: RTMPStream

    override init() {
        stream = RTMPStream(connection: connection)
        super.init()
        connection.addEventListener(.rtmpStatus, selector: #selector(handleRTMPStatus(_:)), observer: self)
        connection.addEventListener(.ioError, selector: #selector(handleIOError(_:)), observer: self)
    }

    func connect(to url: String) {
        lastError = nil
        status = .connecting
        configureCaptureSession()
        connection.connect(url)
    }

    func startPublishing(streamKey: String) {
        stream.publish(streamKey)
        status = .publishing
    }

    func stopPublishing() {
        stream.close()
        connection.close()
        status = .stopped
    }

    private func configureCaptureSession() {
        let audioDevice = AVCaptureDevice.default(for: .audio)
        let cameraDevice = AVCaptureDevice.default(.builtInWideAngleCamera, for: .video, position: .front)
        stream.attachAudio(audioDevice)
        stream.attachCamera(cameraDevice)
    }

    @objc private func handleRTMPStatus(_ notification: Notification) {
        guard let event = Event.from(notification) else {
            return
        }
        if let data = event.data as? ASObject,
           let code = data["code"] as? String,
           code == "NetConnection.Connect.Success" {
            status = .connected
        }
    }

    @objc private func handleIOError(_ notification: Notification) {
        lastError = "RTMP connection error."
        status = .failed
    }
}
