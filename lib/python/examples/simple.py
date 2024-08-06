#!/usr/bin/python3 -B

# Copyright 2023 mjbots Robotic Systems, LLC.  info@mjbots.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
This example commands a single servo at ID #1 using the default
transport to hold the current position indefinitely, and prints the
state of the servo to the console.
"""

import asyncio
import math
import moteus
import time
import argparse

async def main(pos, id=1):
    # By default, Controller connects to id 1, and picks an arbitrary
    # CAN-FD transport, prefering an attached fdcanusb if available.
    c = moteus.Controller(id=id)
    c.make_stay_within(maximum_torque=0.1)
    time.sleep(1)
    state = await c.set_position(position=pos, query=True)
    time.sleep(0.1)
    print(state)
    print()
    time.sleep(1)
    await  c.set_stop()

    time.sleep(2)    
    c2 = moteus.Controller(id=2)
    c2.make_stay_within(maximum_torque=0.1)
    time.sleep(1)
    print("about to test positioning!")
    state = await c2.set_position(position=pos, query=True)
    time.sleep(0.1)
    print(state)
    print()
    time.sleep(1)
    await  c2.set_stop()
    time.sleep(2)
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Control Moteus motor positions")
    parser.add_argument("-p", "--position", type=float, default=0.0)  
    parser.add_argument("-d", "--id", type=int, default=1)  

    args = parser.parse_args()
    pos = args.position
    id = args.id
    asyncio.run(main(pos, id))
