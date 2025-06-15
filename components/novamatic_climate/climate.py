import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import climate_ir
from esphome.const import CONF_ID

AUTO_LOAD = ["climate_ir", "remote_base"]

novamatic_climate_ns = cg.esphome_ns.namespace("novamatic_climate")
NovamaticClimate = novamatic_climate_ns.class_("NovamaticClimate", climate_ir.ClimateIR)

CONFIG_SCHEMA = climate_ir.climate_ir_schema(NovamaticClimate)


async def to_code(config):
    await climate_ir.new_climate_ir(config)
