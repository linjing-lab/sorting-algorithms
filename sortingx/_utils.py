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

from ._typing import Iterable, Callable, Optional, _T, SupportsRichComparison

def generate(__iterable: Iterable[_T], key: Optional[Callable[[_T], SupportsRichComparison]]=None) -> list:
    compare = list(map(key, __iterable)) if key != None else __iterable
    compare = ([[value] for value in compare] if (compare and not isinstance(compare[0], Iterable)) else compare) if key != None else __iterable
    return compare

def core(left: Iterable[_T], right: Iterable[_T], key: Optional[Callable[[_T], SupportsRichComparison]]=None, reverse: bool=False) -> bool:
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

def convert(__iterable: Iterable[_T]) -> list:
    if isinstance(__iterable, (tuple, str, set, dict)):
        return list(__iterable)
    return __iterable