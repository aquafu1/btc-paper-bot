# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 4:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 659 windows, 18207 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 343 | 34.1 | 35.4 | $-267.49 | -7.8% | $732.51 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1542 | 50.6 | 49.7 | $-365.45 | -2.4% | $634.55 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1867 | 51.5 | 50.9 | $-533.32 | -2.9% | $466.68 | -1.2 | done | can't tell from luck |
| trend_filter | 1058 | 50.6 | 51.0 | $-534.96 | -5.1% | $465.04 | -1.7 | done | can't tell from luck |
| value_ev10 | 838 | 38.2 | 39.5 | $-615.05 | -7.3% | $384.95 | -1.8 | done | can't tell from luck |
| value_ev5 | 1266 | 40.8 | 41.4 | $-690.41 | -5.5% | $309.59 | -1.7 | done | can't tell from luck |
| coinflip | 2628 | 50.2 | 50.5 | $-1160.40 | -4.4% | $-160.40 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1542 | 49.4 | 51.3 | $-1240.45 | -8.0% | $-240.45 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1867 | 48.5 | 50.1 | $-1283.99 | -6.9% | $-283.99 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2628 | 50.9 | 51.8 | $-1370.16 | -5.2% | $-370.16 | -2.8 | done | losing for real |
| always_up | 2628 | 47.6 | 49.8 | $-2162.45 | -8.2% | $-1162.45 | -4.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4133 | 48.4 | 49.3 | $-2438.21 |
| ETH | 4540 | 48.3 | 48.7 | $-2748.03 |
| SOL | 4741 | 48.2 | 48.8 | $-2812.59 |
| XRP | 4793 | 48.6 | 48.6 | $-2225.28 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
