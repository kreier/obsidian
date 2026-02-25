# Update workflow

Whenever you make changes in your Quartz repository and want them to show up in Obsidian, you just need two commands:

## In Quartz: Update the "split" branch.

```Bash
git subtree split --prefix=content -b split-content-history
```

## In Obsidian: Pull the changes.

```Bash
git subtree pull --prefix=vault/saiht quartz-origin split-content-history
```
