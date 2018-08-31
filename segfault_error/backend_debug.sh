#!/usr/bin/env bash

# Test all matplotlib backends to debug a segfault issue.

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Copyright (c) 2018, Jed Frey.

# ./backend_debug.sh `which python`

PYTHON=${1:-`which python3`}

echo Python: ${PYTHON}

# Check all matplotlib backends
for MPL_BACKEND in Qt5Agg ipympl GTK3Agg macosx TkAgg nbAgg WebAgg GTK3Cairo Qt4Agg GTKAgg GTKCairo WXAgg
do
	${PYTHON} backend_debug.py ${MPL_BACKEND}
done

