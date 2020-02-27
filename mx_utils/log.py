# AUTOGENERATED! DO NOT EDIT! File to edit: 05_log.ipynb (unless otherwise specified).

__all__ = ['supress_warnings']

# Cell
def supress_warnings(categories=[]):
  "Supress python warnings either all [] or specific `catagories` of warning"
  import warnings
  if cats == []: warnings.filterwarnings("ignore")
  else:
    for cat in categories:
      warnings.filterwarnings(action="ignore", category=cat)