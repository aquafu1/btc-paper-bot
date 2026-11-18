# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 2:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 699 windows, 19331 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 371 | 34.0 | 34.9 | $-259.86 | -7.0% | $740.14 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1628 | 50.2 | 49.4 | $-481.24 | -3.0% | $518.76 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 1986 | 51.7 | 50.8 | $-518.75 | -2.6% | $481.25 | -1.2 | done | can't tell from luck |
| value_ev10 | 895 | 38.2 | 39.1 | $-544.89 | -6.1% | $455.11 | -1.5 | done | can't tell from luck |
| value_ev5 | 1345 | 40.7 | 41.1 | $-630.11 | -4.7% | $369.89 | -1.5 | done | can't tell from luck |
| trend_filter | 1128 | 50.2 | 50.9 | $-646.36 | -5.7% | $353.64 | -2.0 | done | can't tell from luck |
| coinflip | 2788 | 50.1 | 50.3 | $-1226.76 | -4.4% | $-226.76 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1628 | 49.8 | 51.4 | $-1251.93 | -7.7% | $-251.93 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1986 | 48.3 | 49.9 | $-1420.36 | -7.2% | $-420.36 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2788 | 50.9 | 51.8 | $-1506.45 | -5.4% | $-506.45 | -2.9 | done | losing for real |
| always_up | 2788 | 47.4 | 49.5 | $-2343.14 | -8.4% | $-1343.14 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4382 | 48.2 | 49.1 | $-2598.53 |
| ETH | 4815 | 48.2 | 48.5 | $-2779.16 |
| SOL | 5042 | 48.1 | 48.6 | $-2983.22 |
| XRP | 5092 | 48.6 | 48.4 | $-2468.94 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
