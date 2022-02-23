<!---
Copyright 2022 Rafael Schmidt. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Tax Treaty Provisions to Code

This repository is an attempt to transpose and automate the application of Double Taxation Treaty provisions based on the OECD Model Tax Convention (2017).

Articles transposed:

* Article 4: Residence.
* Article 7: Business Profits.
* Article 15: Employment Income.

These models obtain information from the user and extract key aspects of the user inputs using the 🤗 Transformers library via question-answering tasks.

## Examples

Here are a few examples from "residence.py" in order to illustrate how the program works and the information it expects from the user:

```python
>>> python residence.py
====================================================================================================

Please provide the case facts (subject name, individual or entity, residence, permanent home, CIV, 
habitual abode and nationality).

User: Rafael Schmidt is an individual with residence both in Chile and Argentina, where he has also
his permanent homes. His center of vital interests lie only in Argentina where he has his family 
and friends.
====================================================================================================

Please indicate whether your subject is liable to tax or not.

User (Yes/No): Yes

Rafael Schmidt is an individual and is resident both in Chile and Argentina. The tiebreaker rules 
from Article 4(2) are applicable.

(1) According to the information provided, Rafael Schmidt has a permanent home both in Chile and
Argentina. 
Hence, pursuant to Article 4(2)(a), it must be determined where his center of vital interests lie.

(2) According to the information provided, Rafael Schmidt has his/her center of vital interests 
only in Argentina.
Hence, pursuant to Article 4(2)(a), Rafael Schmidt shall be considered to be a resident of Argentina.
====================================================================================================
```

The module outputs a complete analysis of the tiebreaker rules established in Article 4(2) OECD MTC (2017) based on the input given by the user in natural language.

## Limitations

1. Quality of output depends on the model used.
2. Quality of output depends on input given.

## Credits

Rafael Schmidt.
