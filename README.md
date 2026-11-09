# btc-paper-bot

A **paper-trading** bot (fake money, no wallet, no keys) for Polymarket's 15-minute
"Bitcoin Up or Down" markets. It answers one question: **would any of these strategies
actually make money?**

## Where to look

| File | What it is |
|---|---|
| [`results/LEADERBOARD.md`](results/LEADERBOARD.md) | Live paper results per strategy (updated every 15 min) |
| [`results/backtest_report.md`](results/backtest_report.md) | How each strategy did on the last ~3 weeks of real BTC data |
| [`results/trades.csv`](results/trades.csv) | Every fake trade |
| [`results/run_log.csv`](results/run_log.csv) | What the bot did on each run (good for spotting errors) |

## How it works

- **Every ~15 min** (GitHub Actions, free on public repos) the bot:
  1. settles finished trades using Coinbase BTC-USD prices (Up = BTC closed the 15 min at or above where it opened)
  2. looks up the real Polymarket odds for the new window and has each strategy pick Up / Down / skip
  3. logs a fake $10 trade per pick at the real Polymarket price (falls back to an assumed 51c if the market can't be found)
- **Backtest** runs whenever `bot/strategies.py` changes, or manually from the Actions tab.

## Is it profitable? How to tell

- A $1 share bought at 51c needs to win **more than ~51.8%** of the time (after the estimated 1.5% fee) just to break even.
- Ignore any strategy with under **~300 trades** — short streaks are mostly luck.
- It must beat **`coinflip`**, the control group.
- The **Verdict** column flags win rates 2+ standard errors above break-even. Even then, let it run another week.
- Backtest results assume a fixed 51c price, which is too generous. Trust the live leaderboard more.

## Notes

- Polymarket resolves these markets with Chainlink's BTC price; this bot uses Coinbase, so a few near-flat windows may settle differently.
- Fee (`FEE_RATE`) and stake are in `bot/config.py`.
- Nothing here places real trades.
