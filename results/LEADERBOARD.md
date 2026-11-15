# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 7:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 383 windows, 10456 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 10:00 PM | too few trades (196/200) |
| value_ev10 | 505 | 39.8 | 40.5 | $-237.29 | -4.7% | $762.71 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 876 | 50.2 | 49.8 | $-314.40 | -3.6% | $685.60 | -1.1 | done | can't tell from luck |
| value_ev5 | 745 | 41.5 | 42.1 | $-366.06 | -4.9% | $633.94 | -1.2 | done | can't tell from luck |
| trend_filter | 583 | 48.7 | 50.5 | $-466.85 | -8.0% | $533.15 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1047 | 51.3 | 52.1 | $-581.05 | -5.5% | $418.95 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1047 | 48.7 | 49.7 | $-592.75 | -5.7% | $407.25 | -1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 876 | 49.8 | 52.0 | $-723.13 | -8.3% | $276.87 | -2.6 | done | losing for real |
| coinflip | 1527 | 50.0 | 50.8 | $-811.70 | -5.3% | $188.30 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1527 | 49.3 | 51.5 | $-1197.02 | -7.8% | $-197.02 | -3.2 | done | losing for real |
| always_up | 1527 | 45.5 | 50.7 | $-2110.88 | -13.8% | $-1110.88 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2359 | 47.4 | 49.4 | $-1873.21 |
| ETH | 2629 | 47.5 | 48.9 | $-1928.13 |
| SOL | 2703 | 47.8 | 49.4 | $-2084.90 |
| XRP | 2765 | 48.5 | 49.1 | $-1541.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
