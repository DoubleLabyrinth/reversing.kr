#!/usr/bin/env python

Name = [ 0 ] * 4
Serial = '76876-77776'

Name[0] = pow(2, 0) * 0 + pow(2, 3) * 0 + pow(2, 1) * 1 + pow(2, 2) * 0 + pow(2, 4) * 0 + 96
Name[1] = pow(2, 2) * 1 + pow(2, 3) * 0 + pow(2, 4) * 1 + pow(2, 0) * 1 + pow(2, 1) * 0 + 96
Name[2] = pow(2, 0) * 1 + pow(2, 3) * 1 + pow(2, 1) * 0 + pow(2, 2) * 1 + pow(2, 4) * 0 + 96
Name[3] = pow(2, 2) * 0 + pow(2, 3) * 0 + pow(2, 4) * 1 + pow(2, 0) * 0 + pow(2, 1) * 0 + 96
print(bytes(Name).decode())
