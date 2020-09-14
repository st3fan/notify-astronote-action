# Notify AstroNote Action

Send workflow status notifications to your Apple Watch through [AstroNote](https://astronote.app).

### Example workflow

```yaml
steps:
  - uses: st3fan/notify-astronote-action@master
    if: always()
    with:
      status: ${{ job.status }}
      notify_when: 'failure' # default: 'success,failure,warnings'
    env:
      ASTRONOTE_TOKEN: ${{ secrets.ASTRONOTE_TOKEN }} # required
```

