# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 9:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1397 windows, 36054 settled trades, 386 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 724 | 34.7 | 35.4 | $-493.87 | -6.8% | $506.13 | -1.4 | done | can't tell from luck |
| value_ev10 | 1749 | 38.9 | 39.2 | $-768.67 | -4.4% | $231.33 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3601 | 50.8 | 50.1 | $-1019.52 | -2.8% | $-19.52 | -1.7 | done | can't tell from luck |
| value_ev5 | 2636 | 40.6 | 41.1 | $-1240.13 | -4.7% | $-240.13 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 3024 | 49.3 | 49.3 | $-1462.42 | -4.8% | $-462.42 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 3024 | 50.7 | 50.9 | $-1580.49 | -5.2% | $-580.49 | -2.9 | done | losing for real |
| trend_filter | 2143 | 48.6 | 50.4 | $-1871.37 | -8.7% | $-871.37 | -4.1 | done | losing for real |
| coinflip | 5184 | 50.0 | 50.0 | $-2226.14 | -4.3% | $-1226.14 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3601 | 49.2 | 50.2 | $-2244.52 | -6.2% | $-1244.52 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5184 | 50.2 | 51.3 | $-3207.62 | -6.2% | $-2207.62 | -4.6 | done | losing for real |
| always_up | 5184 | 47.9 | 49.3 | $-3690.47 | -7.1% | $-2690.47 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9028 | 48.1 | 48.8 | $-4951.63 |
| ETH | 9716 | 48.1 | 48.1 | $-5269.36 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
