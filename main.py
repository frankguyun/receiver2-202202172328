def on_received_string(receivedString):
    global signal
    serial.write_number(int(Math.map(signal, -95, -28, 0, 200)))
    signal = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)
    led.plot_bar_graph(Math.map(signal, -95, -28, 0, 9), 9)
radio.on_received_string(on_received_string)

signal = 0
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)
radio.set_group(1)