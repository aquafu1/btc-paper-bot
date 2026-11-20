# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 12:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 930 windows, 25694 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1161 | 38.2 | 39.1 | $-632.90 | -5.5% | $367.10 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2193 | 50.1 | 49.8 | $-923.02 | -4.2% | $76.98 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2623 | 50.9 | 50.6 | $-923.49 | -3.5% | $76.51 | -1.8 | done | can't tell from luck |
| value_ev5 | 1763 | 39.8 | 41.0 | $-1047.33 | -5.9% | $-47.33 | -2.1 | done | losing for real |
| trend_filter | 1527 | 49.9 | 51.0 | $-1065.88 | -7.0% | $-65.88 | -2.8 | done | losing for real |
| coinflip | 3712 | 50.4 | 50.4 | $-1523.72 | -4.1% | $-523.72 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2193 | 49.9 | 50.9 | $-1525.41 | -7.0% | $-525.41 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 2623 | 49.1 | 50.3 | $-1607.33 | -6.1% | $-607.33 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3712 | 50.9 | 51.6 | $-1898.16 | -5.1% | $-898.16 | -3.2 | done | losing for real |
| always_up | 3712 | 46.8 | 49.7 | $-3790.84 | -10.2% | $-2790.84 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5851 | 48.2 | 49.1 | $-3380.73 |
| ETH | 6392 | 48.2 | 48.6 | $-3979.96 |
| SOL | 6704 | 48.2 | 48.6 | $-3917.55 |
| XRP | 6747 | 48.3 | 48.5 | $-3805.57 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
