# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 10:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 587 windows, 16249 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1384 | 51.2 | 49.6 | $-238.21 | -1.7% | $761.79 | -0.6 | done | can't tell from luck |
| value_ev20 | 317 | 33.1 | 35.3 | $-362.24 | -11.4% | $637.76 | -1.6 | done | can't tell from luck |
| trend_filter | 946 | 50.3 | 50.9 | $-524.37 | -5.5% | $475.63 | -1.7 | done | can't tell from luck |
| value_ev10 | 761 | 37.5 | 39.5 | $-733.78 | -9.6% | $266.22 | -2.2 | done | losing for real |
| value_ev5 | 1139 | 40.1 | 41.3 | $-830.53 | -7.3% | $169.47 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1649 | 50.8 | 51.0 | $-856.08 | -5.2% | $143.92 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1649 | 49.2 | 49.9 | $-919.16 | -5.6% | $80.84 | -2.3 | done | losing for real |
| coinflip | 2340 | 49.9 | 50.5 | $-1258.76 | -5.4% | $-258.76 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1384 | 48.8 | 51.3 | $-1335.19 | -9.6% | $-335.19 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2340 | 50.1 | 51.8 | $-1670.16 | -7.1% | $-670.16 | -3.6 | done | losing for real |
| always_up | 2340 | 47.3 | 49.9 | $-2238.22 | -9.6% | $-1238.22 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3690 | 47.8 | 49.2 | $-2708.52 |
| ETH | 4057 | 48.0 | 48.6 | $-2736.06 |
| SOL | 4219 | 47.8 | 48.8 | $-3147.96 |
| XRP | 4283 | 48.4 | 48.6 | $-2374.16 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
