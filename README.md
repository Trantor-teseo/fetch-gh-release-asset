# Fetch GH Release Asset

This action downloads an asset from a Github release. Private repos are supported.

Original action is now converted to Python script.

## Inputs

### `repo`

**Required** The `org/repo`. Defaults to the current repo.

### `version`

The release version to fetch from. Default `"latest"`. If not `"latest"`, this has to be in the form `tags/<tag_name>` or `<release_id>`.

### `file`

**Required** The name of the file in the release.

### `token`
**Required** Personal Access Token to access repository. You need to either specify this or set the GITHUB_TOKEN environment variable yourself.

## Example usage

```yaml
uses: dsaltares/fetch-gh-release-asset@master
with:
  repo: "dsaltares/godot-wild-jam-18"
  version: "latest"
  file: "plague-linux.zip"
  token: ${{ secrets.YOUR_TOKEN }}
```
