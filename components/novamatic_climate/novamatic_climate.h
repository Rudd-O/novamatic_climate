#pragma once

#include "esphome/components/climate_ir/climate_ir.h"
#include "esphome/components/remote_base/pronto_protocol.h"

namespace esphome
{
    namespace novamatic_climate
    {
        struct ModeSelector
        {
            esphome::climate::ClimateMode mode;
            esphome::climate::ClimateFanMode fan_mode;
            esphome::climate::ClimateSwingMode swing_mode;
            float temp;
        };

        // Temperature
        const uint8_t TEMP_MIN = 16; // Celsius
        const uint8_t TEMP_MAX = 30; // Celsius

        class NovamaticClimate : public climate_ir::ClimateIR
        {
        public:
            NovamaticClimate()
                : climate_ir::ClimateIR(TEMP_MIN, TEMP_MAX, 1.0f, true, true,
                                        {climate::CLIMATE_FAN_AUTO, climate::CLIMATE_FAN_LOW, climate::CLIMATE_FAN_MEDIUM,
                                         climate::CLIMATE_FAN_HIGH},
                                        {climate::CLIMATE_SWING_OFF, climate::CLIMATE_SWING_VERTICAL}) {}

        protected:
            /// Transmit via IR the state of this climate controller.
            void transmit_state() override;
            esphome::climate::ClimateTraits traits() override;

        private:
            void transmit_(const struct esphome::remote_base::ProntoData);
            struct ModeSelector *last_valid_selector = nullptr;
        };

    } // namespace climate_ir_lg
} // namespace esphome