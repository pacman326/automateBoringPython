#vampire2.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Paul Coroneos
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

print('What is your name?')
name = input()
print('How old are you?')
age = int(input())
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice kiddo.')
elif age > 100:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 2000:
    print('You are not Alice, granny.')
