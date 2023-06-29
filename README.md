# FUST Novamatic CL 1590 for ESPHome

This project integrates a Novamatic CL 1590 portable mini-split
air conditioning unit, through its infrared port and a small
ESP8285 microcontroller with infrared transmitter on board
(typically board type `esp01_m` on ESPHome).  It supports all
modes and temperature targets of the air conditioner unit.

## Will this work with my A/C unit?

The remote control this climate component simulates is model
number AR-715 (parts code IR30-0168CN---B), so check your
A/C unit's remote — if it matches, this is for you: you got
yourself a smart A/C unit now.

## Will this work with my ESP device?

Probably, so long as it has an infrared transmitter that can
do 38 KHz.
[This is the unit I got](https://de.aliexpress.com/item/1005001598129325.html).
It works perfectly with the code as it ships.

If your transmitter doesn't do 38 KHz by default, you may have
to adjust the code to change the default frequency of your unit,
as the code does not do this currently.  Right after
`auto *data = transmit.get_data();` in `novamatic_climate.cpp`
you may add `data->set_carrier_frequency(38000);` to achieve
that effect.

## How do I program the circuit?

Use your own version of this sample ESPHome sketch:

```yaml
esphome:
  name: ir-transceiver
  friendly_name: IR transceiver

external_components:
  - source:
      type: git
      url: https://github.com/Rudd-O/novamatic_climate
      ref: master
    components:
    - novamatic_climate

esp8266:
  # ESP8285 IR transceiver
  board: esp01_1m

# Enable logging
logger:
  level: debug

# Enable Home Assistant API
api:
  encryption:
    key: !secret api_key
  services:
  - service: send_pronto
    variables:
      data: string
    then:
    - remote_transmitter.transmit_pronto:
        data: !lambda 'return data;'

ota:
  password: !secret ota_password

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password

button:
- platform: restart
  name: Restart
  entity_category: diagnostic
  icon: mdi:restart
- platform: safe_mode
  name: Safe mode restart
  entity_category: diagnostic
  icon: mdi:restart-alert

climate:
- platform: novamatic_climate
  name: Novamatic CL 1590
  supports_heat: false
  transmitter_id: transmitter
  icon: mdi:air-conditioner

remote_receiver:
  id: receiver
  pin:
    number: GPIO14
    inverted: True
  dump: pronto

remote_transmitter:
  id: transmitter
  pin: GPIO4
  carrier_duty_percent: 50%

sensor:
- platform: wifi_signal
  name: "Wi-Fi signal strength"
  update_interval: 10s
  entity_category: "diagnostic"
```

## Notes

The `supports_heat` and `supports_cool` configuration keys are
wholly ignored and overridden by the code.