radio.onReceivedString(function (receivedString) {
    serial.writeNumber(Math.trunc(Math.map(signal, -95, -28, 0, 200)))
    signal = radio.receivedPacket(RadioPacketProperty.SignalStrength)
    led.plotBarGraph(
    Math.map(signal, -95, -28, 0, 9),
    9
    )
})
let signal = 0
serial.redirect(
SerialPin.USB_TX,
SerialPin.USB_RX,
BaudRate.BaudRate115200
)
radio.setGroup(1)
