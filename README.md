TLDR; run scripts from the project root with -m flag

For example, with the directory structure below
```
algorithm_study
├── sorting
│ ├── quickselect.py
│ └── partition.py 
└── trees
 ├── traversal.py 
 └── bst.py 
```
I could run `quickselect.py` from `algorithm_study` with
> `python3 -m sorting.quickselect`

This causes imports to be relative to the top-level dir, allowing for intuitive importing of sibling modules. E.g. 

> ```
> # quickselect.py
> from sorting import partition
> from trees import binary_search 
> ```


