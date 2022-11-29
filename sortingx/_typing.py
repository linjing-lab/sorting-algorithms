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

from typing import (
    Any,
    Iterable,
    Callable,
    Optional,
    Protocol,
    TypeVar, 
    Union,
    List
)

from typing_extensions import (
    TypeAlias
)

_T = TypeVar("_T")

_T_contra = TypeVar("_T_contra", contravariant=True)

class SupportsDunderLT(Protocol[_T_contra]):
    def __lt__(self, __other: _T_contra) -> bool: ...

class SupportsDunderGT(Protocol[_T_contra]):
    def __gt__(self, __other: _T_contra) -> bool: ...
    
SupportsRichComparison: TypeAlias = Union[SupportsDunderLT[Any], SupportsDunderGT[Any]]