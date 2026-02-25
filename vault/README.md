# Creation and update workflow

## Quartz: create a "split" branch with only my commits

```Bash
# Finds the first commit you made and only splits from there onwards
git subtree split --prefix=content fc2b583..HEAD -b split-content-history
```


## In Quartz: Update the "split" branch.

```Bash
git subtree split --prefix=content -b split-content-history
```

## In Obsidian: Pull the changes.

```Bash
git subtree pull --prefix=vault/saiht quartz-origin split-content-history
```
