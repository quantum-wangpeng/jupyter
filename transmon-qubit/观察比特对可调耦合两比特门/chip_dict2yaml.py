# -*- coding: utf-8 -*-
# @Time     : 2022/9/19 15:27
# @Author   : WTL
# @Software : PyCharm
import yaml

CHIP_DICT = {
        'qubits': {
            'Q1': {
                'w_idle': 4.6,
                'eta': -220e-3
            },
            'C1': {
                'w_idle': 7.,
                'eta': -200e-3
            },
            'Q2': {
                'w_idle': 5.0,
                'eta': -220e-3
            },
            'C2': {
                'w_idle': 7.,
                'eta': -200e-3
            },
            'Q3': {
                'w_idle': 4.6,
                'eta': -220e-3
            },
       
        },

        'rho_map': {
            'Q1-C1': 0.031,
            'Q2-C1': 0.031,
            'Q1-Q2': 0.0034,
            
            'Q2-C2': 0.031,
            'Q3-C2': 0.031,
            'Q2-Q3': 0.0034,
        }
    }

if __name__ == '__main__':
    CHIP_YAML = yaml.dump(CHIP_DICT)

    with open('chip_param.yaml', 'w') as f:
        yaml.dump(CHIP_DICT, f, sort_keys=False)

    # with open(r'F:\miracle\AutoTest\config\exp.yaml', 'r') as f:
    #     y = yaml.load(f.read(), Loader=yaml.Loader)
    #     print(y)

