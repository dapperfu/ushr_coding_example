# Workaround for edge case error.

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

import matplotlib as mpl
import sys

backend = sys.argv[1]
print("Backend: {}".format(backend))
mpl.use(backend)  # or whatever other backend that you want

import matplotlib.pyplot as plt
import numpy as np

X = np.arange(0, 10)
Y = np.arange(0, 10)

plt.plot(X, Y, color="red")  # current X-Axis
plt.plot(X, 2 * Y, color="green")  # current Y-Axis
plt.grid(True)
plt.axes().set_aspect("equal")
plt.show()
