# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 12:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1120 windows, 31016 settled trades, 33 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 591 | 34.5 | 35.1 | $-359.77 | -6.1% | $640.23 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3127 | 51.1 | 50.4 | $-833.74 | -2.7% | $166.26 | -1.5 | done | can't tell from luck |
| value_ev10 | 1448 | 38.1 | 39.2 | $-886.97 | -6.1% | $113.03 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2631 | 49.7 | 49.4 | $-1098.70 | -4.2% | $-98.70 | -2.1 | done | losing for real |
| value_ev5 | 2192 | 40.1 | 41.1 | $-1262.09 | -5.8% | $-262.09 | -2.3 | done | losing for real |
| trend_filter | 1841 | 49.2 | 50.4 | $-1378.74 | -7.5% | $-378.74 | -3.3 | done | losing for real |
| reversal_60m_0.30pct | 2631 | 50.3 | 51.1 | $-1689.25 | -6.4% | $-689.25 | -3.4 | done | losing for real |
| coinflip | 4476 | 50.4 | 50.2 | $-1797.48 | -4.0% | $-797.48 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 3127 | 48.9 | 50.2 | $-2077.57 | -6.6% | $-1077.57 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4476 | 50.5 | 51.4 | $-2548.95 | -5.7% | $-1548.95 | -3.9 | done | losing for real |
| always_up | 4476 | 47.7 | 49.3 | $-3433.86 | -7.7% | $-2433.86 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7111 | 48.4 | 49.0 | $-3602.67 |
| ETH | 7686 | 48.1 | 48.4 | $-4634.75 |
| SOL | 8066 | 48.0 | 48.4 | $-4543.05 |
| XRP | 8153 | 48.2 | 48.2 | $-4586.67 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
