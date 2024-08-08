# GitHub action. Replace string in file

This action find an replace specific string in given file.

## Inputs

## `file-path`

**Required** File path where changes should be done.

## `search`

**Required** String that should be replaced.

## `replace`

**Required** New string.

## Example usage

```
uses: devapro/replace-string-action@v0.0.8
with:
  file-path: "project/build.gradle.kts"
  search: "buildVersionCode = 111"
  replace: "buildVersionCode = 222"
```
