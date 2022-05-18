#!/usr/bin/env python
# coding: utf-8

import yaml

def format(var_verilog,var_fpga):
    return f'set_property IOSTANDARD LVCMOS33 [get_ports {var_verilog}]\nset_property PACKAGE_PIN {var_fpga} [get_ports {var_verilog}]\n'

with open('xdc.yml','r') as f:
    config=yaml.safe_load(f)

with open('top.xdc','w') as f:
    for var_verilog in config:
        if(type(config[var_verilog])==type([])):
            l=len(config[var_verilog])
            for i in range(l):
                vv=f'{{{var_verilog}[{l-1-i}]}}'
                vf=config[var_verilog][i]
                f.write(format(vv,vf))
        else:
            f.write(format(var_verilog,config[var_verilog]))
            



