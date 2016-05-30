# ghcollector

## Usage

```shell
$ python stars.py [personal_access_token]
$ python stars.py [personal_access_token] | tee stars.tsv
```

`personal_access_token` only requires public access.

if `personal_access_token` is not specified, works as an unauthorized user,
which is not recommended.

## Output

Print Recent 100 starred repos of all users to stdout
formatted in `<user>\t<repo>`

```
mojombo crystal-lang/crystal
mojombo mojombo/jquery
...
defunkt gillesdemey/Cumulus
defunkt apple/swift
defunkt nylas/N1
...
```

## Rate Limiting

[Rating Limiting](https://developer.github.com/v3/#rate-limiting)

it waits for reset when it reaches `rate limit`


```
# These are printed to stderr
...
wait for reset: 469s remaining
wait for reset: 468s remaining
wait for reset: 467s remaining
wait for reset: 466s remaining
wait for reset: 465s remaining
wait for reset: 464s remaining
wait for reset: 463s remaining
wait for reset: 462s remaining
...
```
