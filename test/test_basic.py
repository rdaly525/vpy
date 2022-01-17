from vpy import parse_verilog



def test_basic():
    file = 'test/vlog/basic.v'
    parse_verilog(file)
    return