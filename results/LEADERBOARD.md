# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 7:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1197 windows, 33070 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 646 | 34.7 | 35.3 | $-408.79 | -6.3% | $591.21 | -1.2 | done | can't tell from luck |
| value_ev10 | 1576 | 38.5 | 39.2 | $-852.09 | -5.4% | $147.91 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3313 | 50.8 | 50.3 | $-1058.58 | -3.2% | $-58.58 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2772 | 49.5 | 49.4 | $-1269.44 | -4.6% | $-269.44 | -2.4 | done | losing for real |
| value_ev5 | 2386 | 40.3 | 41.1 | $-1298.67 | -5.4% | $-298.67 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 2772 | 50.5 | 51.1 | $-1665.31 | -6.0% | $-665.31 | -3.2 | done | losing for real |
| trend_filter | 1952 | 48.7 | 50.5 | $-1684.02 | -8.6% | $-684.02 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3313 | 49.2 | 50.3 | $-2074.07 | -6.3% | $-1074.07 | -3.6 | done | losing for real |
| coinflip | 4780 | 50.1 | 50.2 | $-2124.00 | -4.4% | $-1124.00 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4780 | 50.1 | 51.4 | $-3044.24 | -6.4% | $-2044.24 | -4.5 | done | losing for real |
| always_up | 4780 | 47.8 | 49.3 | $-3548.65 | -7.4% | $-2548.65 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7593 | 48.1 | 48.9 | $-4344.29 |
| ETH | 8200 | 48.0 | 48.4 | $-5084.55 |
| SOL | 8612 | 48.2 | 48.4 | $-4458.61 |
| XRP | 8665 | 48.1 | 48.2 | $-5140.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
