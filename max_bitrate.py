# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
#  Text explaining script usage
# Parameters:
# tx_w: transimtter power in Watts
# tx_gain_db: transmitter gain in db
# freq_hz: frequency in hz
# dist_km: transmission distance in km
# rx_gain_db: receiver gain in db
# n0_j: spectral density in joules
# bw_hz: bandwidth in hz
# Output:
#  Maximum achiveable bit rate
#
# Written by Chatham Campbell
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
# e.g., R_E_KM = 6378.137

# helper functions

tx_w = float('nan') 
tx_gain_db = float('nan') 
freq_hz = float('nan') 
dist_km = float('nan')
rx_gain_db = float('nan')
n0_j = float('nan')
bw_hz = float('nan')

#parse script arguments
if len(sys.argv)==8:
  tx_w = float(sys.argv[1])
  tx_gain_db = float(sys.argv[2])
  freq_hz = float(sys.argv[3])
  dist_km = float(sys.argv[4])
  rx_gain_db = float(sys.argv[5])
  n0_j = float(sys.argv[6])
  bw_hz = float(sys.argv[7])
else:
  print(\
   'Usage: '\
   'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'
  )
  exit()

# write script below this line
c = 2.99792458*10**8
lambda1 = c/freq_hz

Gt = math.pow((tx_gain_db/10),10)
Gr = math.pow((rx_gain_db/10),10)
Ll = math.pow((-1/10),10)
La = math.pow((0/10),10)

N0 = n0_j * bw_hz

C = tx_w * Ll * Gt *(lambda1/(4*math.pi*dist_km*1000))**2 * La*Gr

r_max = bw_hz * math.log2(1+(C/N0))

print(math.floor(r_max))

