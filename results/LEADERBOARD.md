# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 9:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1204 windows, 33203 settled trades, 152 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 649 | 34.5 | 35.3 | $-438.79 | -6.8% | $561.21 | -1.3 | done | can't tell from luck |
| value_ev10 | 1586 | 38.6 | 39.2 | $-830.46 | -5.2% | $169.54 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3327 | 50.8 | 50.3 | $-1076.68 | -3.2% | $-76.68 | -1.9 | done | can't tell from luck |
| value_ev5 | 2397 | 40.4 | 41.1 | $-1269.26 | -5.3% | $-269.26 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2781 | 49.5 | 49.4 | $-1275.79 | -4.6% | $-275.79 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2781 | 50.5 | 51.1 | $-1676.56 | -6.0% | $-676.56 | -3.3 | done | losing for real |
| trend_filter | 1961 | 48.6 | 50.4 | $-1690.37 | -8.6% | $-690.37 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3327 | 49.2 | 50.2 | $-2072.20 | -6.2% | $-1072.20 | -3.6 | done | losing for real |
| coinflip | 4798 | 50.1 | 50.1 | $-2142.07 | -4.5% | $-1142.07 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4798 | 50.2 | 51.4 | $-2969.09 | -6.2% | $-1969.09 | -4.4 | done | losing for real |
| always_up | 4798 | 47.9 | 49.3 | $-3473.51 | -7.2% | $-2473.51 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7638 | 48.1 | 48.9 | $-4339.48 |
| ETH | 8255 | 48.1 | 48.3 | $-4991.07 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
