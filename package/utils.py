# Copyright 2022 linjing-lab
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .typing import Iterable, Callable

def generate(array: Iterable, key: Callable=None) -> list:
    compare = list(map(key, array)) if key != None else array
    compare = ([[value] for value in compare] if compare and compare[0] is not list else compare) if key != None else array
    return compare

def core(left: list, right: list, key: Callable=None, reverse: bool=False) -> bool:
    if key == None:
        return left < right if reverse else left > right
    for index in range(0, len(left)):
        if left[index] > right[index] and reverse:
            return False
        elif left[index] > right[index] and not reverse:
            return True
        elif left[index] < right[index] and reverse:
            return True
        elif left[index] < right[index] and not reverse:
            return False
    return False