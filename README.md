# btc-paper-bot

A **paper-trading** bot (fake money, no wallet, no keys) for Polymarket's 15-minute
"Up or Down" crypto markets (BTC, ETH, SOL, XRP). It answers one question:
**would any of these strategies actually make money?**

## Where to look

| File | What it is |
|---|---|
| [`results/LEADERBOARD.md`](results/LEADERBOARD.md) | Live paper results per strategy (updated every few minutes) |
| [`results/backtest_report.md`](results/backtest_report.md) | How each strategy did on the last ~3 weeks of real BTC data |
| [`results/trades.csv`](results/trades.csv) | Every fake trade |
| [`results/run_log.csv`](results/run_log.csv) | What the bot did on each wake (good for spotting errors) |

## How it works

- A GitHub Actions job runs a **loop** for ~5.5 hours, then starts the next job itself
  (GitHub's built-in every-15-min timer only fired ~3 times a day, so it isn't used).
- **~20s after each 15-min window opens**, for each coin, each strategy picks Up / Down / skip.
  Each pick is a fake $10 buy, priced by walking the **real Polymarket order book**,
  minus Polymarket's **real taker fee** (`0.07 x shares x p x (1-p)`, read from each market).
- **~5 min after the window opens** it settles the window that just ended using
  **Polymarket's official result** (Chainlink price), not an outside price feed.
- **Backtest** runs whenever the strategy or scoring code changes, or manually from the Actions tab.

## Is it profitable? How to tell

- A strategy makes money only if **Win % beats Break-even %** (break-even is about 52.8%
  at 51c with fees).
- Ignore any strategy with under **200 trades**.
- It must beat **`coinflip`**, the control group.
- The **Verdict** column flags strategies whose average profit is 2+ standard errors above zero.
  Even then, let it run longer before using real money.

## Stopping it

Actions tab -> "Paper trade (loop)" -> "..." -> **Disable workflow**. Nothing here places real trades.
