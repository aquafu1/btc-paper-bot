# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 3:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1086 windows, 30036 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 564 | 34.6 | 35.2 | $-322.67 | -5.7% | $677.33 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 3034 | 51.1 | 50.5 | $-858.66 | -2.8% | $141.34 | -1.6 | done | can't tell from luck |
| value_ev10 | 1389 | 37.8 | 39.2 | $-933.87 | -6.7% | $66.13 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2553 | 49.8 | 49.5 | $-1068.08 | -4.2% | $-68.08 | -2.1 | done | losing for real |
| trend_filter | 1786 | 49.6 | 50.6 | $-1245.66 | -7.0% | $-245.66 | -3.0 | done | losing for real |
| value_ev5 | 2112 | 39.8 | 41.1 | $-1310.00 | -6.2% | $-310.00 | -2.4 | done | losing for real |
| coinflip | 4337 | 50.5 | 50.3 | $-1660.11 | -3.8% | $-660.11 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2553 | 50.2 | 51.1 | $-1676.50 | -6.6% | $-676.50 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3034 | 48.9 | 50.3 | $-2027.95 | -6.7% | $-1027.95 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4337 | 51.0 | 51.5 | $-2076.83 | -4.8% | $-1076.83 | -3.3 | done | losing for real |
| always_up | 4337 | 47.5 | 49.4 | $-3582.59 | -8.3% | $-2582.59 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6862 | 48.5 | 49.0 | $-3307.78 |
| ETH | 7437 | 48.2 | 48.5 | $-4447.27 |
| SOL | 7831 | 48.1 | 48.5 | $-4463.75 |
| XRP | 7906 | 48.3 | 48.3 | $-4544.12 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
