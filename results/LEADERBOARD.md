# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 3:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 749 windows, 20673 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 389 | 33.7 | 34.9 | $-301.39 | -7.7% | $698.61 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 2114 | 51.6 | 50.6 | $-481.19 | -2.3% | $518.81 | -1.0 | done | can't tell from luck |
| value_ev10 | 946 | 37.8 | 39.1 | $-639.74 | -6.8% | $360.26 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1750 | 50.0 | 49.6 | $-655.37 | -3.7% | $344.63 | -1.6 | done | can't tell from luck |
| value_ev5 | 1426 | 40.3 | 41.1 | $-812.97 | -5.7% | $187.03 | -1.8 | done | can't tell from luck |
| trend_filter | 1220 | 49.8 | 50.9 | $-822.88 | -6.7% | $177.12 | -2.4 | done | losing for real |
| coinflip | 2988 | 50.4 | 50.3 | $-1157.82 | -3.9% | $-157.82 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1750 | 50.0 | 51.2 | $-1215.28 | -6.9% | $-215.28 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2114 | 48.4 | 50.2 | $-1557.08 | -7.4% | $-557.08 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2988 | 50.7 | 51.8 | $-1698.90 | -5.7% | $-698.90 | -3.2 | done | losing for real |
| always_up | 2988 | 46.9 | 49.5 | $-2808.10 | -9.4% | $-1808.10 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4681 | 48.1 | 49.1 | $-3009.08 |
| ETH | 5150 | 48.0 | 48.5 | $-3335.61 |
| SOL | 5389 | 48.0 | 48.6 | $-3168.34 |
| XRP | 5453 | 48.5 | 48.5 | $-2637.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
