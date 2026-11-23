# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 7:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1197 windows, 33075 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 646 | 34.7 | 35.3 | $-408.79 | -6.3% | $591.21 | -1.2 | done | can't tell from luck |
| value_ev10 | 1576 | 38.5 | 39.2 | $-852.09 | -5.4% | $147.91 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3314 | 50.8 | 50.3 | $-1068.58 | -3.2% | $-68.58 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2772 | 49.5 | 49.4 | $-1269.44 | -4.6% | $-269.44 | -2.4 | done | losing for real |
| value_ev5 | 2386 | 40.3 | 41.1 | $-1298.67 | -5.4% | $-298.67 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 2772 | 50.5 | 51.1 | $-1665.31 | -6.0% | $-665.31 | -3.2 | done | losing for real |
| trend_filter | 1952 | 48.7 | 50.5 | $-1684.02 | -8.6% | $-684.02 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3314 | 49.2 | 50.3 | $-2069.40 | -6.2% | $-1069.40 | -3.6 | done | losing for real |
| coinflip | 4781 | 50.1 | 50.1 | $-2134.00 | -4.5% | $-1134.00 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4781 | 50.2 | 51.4 | $-3039.56 | -6.4% | $-2039.56 | -4.5 | done | losing for real |
| always_up | 4781 | 47.8 | 49.3 | $-3543.97 | -7.4% | $-2543.97 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7598 | 48.1 | 48.9 | $-4350.26 |
| ETH | 8200 | 48.0 | 48.4 | $-5084.55 |
| SOL | 8612 | 48.2 | 48.4 | $-4458.61 |
| XRP | 8665 | 48.1 | 48.2 | $-5140.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
