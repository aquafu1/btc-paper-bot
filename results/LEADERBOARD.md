# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 2:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 408 windows, 11182 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 202 | 36.1 | 36.5 | $-86.95 | -4.3% | $913.05 | -0.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 953 | 51.1 | 49.9 | $-171.49 | -1.8% | $828.51 | -0.6 | done | can't tell from luck |
| value_ev10 | 524 | 40.3 | 40.5 | $-203.49 | -3.9% | $796.51 | -0.7 | done | can't tell from luck |
| trend_filter | 632 | 50.3 | 50.7 | $-293.07 | -4.6% | $706.93 | -1.2 | done | can't tell from luck |
| value_ev5 | 790 | 42.0 | 42.2 | $-312.64 | -4.0% | $687.36 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1125 | 49.5 | 49.9 | $-486.43 | -4.3% | $513.57 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1125 | 50.5 | 51.9 | $-741.61 | -6.6% | $258.39 | -2.3 | done | losing for real |
| coinflip | 1626 | 50.2 | 50.9 | $-803.41 | -4.9% | $196.59 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 953 | 48.9 | 52.0 | $-915.85 | -9.6% | $84.15 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1626 | 49.9 | 51.6 | $-1074.42 | -6.6% | $-74.42 | -2.8 | done | losing for real |
| always_up | 1626 | 45.6 | 50.7 | $-2169.56 | -13.3% | $-1169.56 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2521 | 47.7 | 49.5 | $-1795.10 |
| ETH | 2814 | 47.9 | 49.0 | $-1727.77 |
| SOL | 2896 | 47.9 | 49.5 | $-2204.19 |
| XRP | 2951 | 48.9 | 49.3 | $-1531.86 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
