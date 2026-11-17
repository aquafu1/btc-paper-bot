# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 12:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 640 windows, 17700 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1496 | 51.1 | 49.6 | $-203.57 | -1.4% | $796.43 | -0.5 | done | can't tell from luck |
| value_ev20 | 333 | 34.2 | 35.3 | $-246.80 | -7.4% | $753.20 | -1.0 | done | can't tell from luck |
| trend_filter | 1023 | 50.5 | 50.8 | $-498.76 | -4.9% | $501.24 | -1.6 | done | can't tell from luck |
| value_ev10 | 814 | 38.5 | 39.5 | $-549.08 | -6.7% | $450.92 | -1.6 | done | can't tell from luck |
| value_ev5 | 1235 | 40.9 | 41.4 | $-644.19 | -5.2% | $355.81 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1822 | 51.1 | 51.0 | $-709.31 | -3.9% | $290.69 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1822 | 48.9 | 50.0 | $-1100.30 | -6.0% | $-100.30 | -2.6 | done | losing for real |
| coinflip | 2553 | 50.2 | 50.5 | $-1146.90 | -4.5% | $-146.90 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1496 | 48.9 | 51.4 | $-1372.04 | -9.2% | $-372.04 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2553 | 50.7 | 51.7 | $-1372.22 | -5.4% | $-372.22 | -2.8 | done | losing for real |
| always_up | 2553 | 47.2 | 49.7 | $-2262.66 | -8.9% | $-1262.66 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4021 | 48.4 | 49.3 | $-2358.63 |
| ETH | 4429 | 48.3 | 48.7 | $-2605.66 |
| SOL | 4593 | 48.0 | 48.8 | $-2882.19 |
| XRP | 4657 | 48.5 | 48.5 | $-2259.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
