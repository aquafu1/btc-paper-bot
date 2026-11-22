# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 12:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1075 windows, 29743 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 554 | 34.3 | 35.1 | $-353.30 | -6.4% | $646.70 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3016 | 51.3 | 50.5 | $-787.73 | -2.6% | $212.27 | -1.4 | done | can't tell from luck |
| value_ev10 | 1371 | 37.6 | 39.2 | $-999.47 | -7.3% | $0.53 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2528 | 49.7 | 49.6 | $-1151.47 | -4.6% | $-151.47 | -2.3 | done | losing for real |
| trend_filter | 1769 | 49.5 | 50.7 | $-1276.23 | -7.2% | $-276.23 | -3.1 | done | losing for real |
| value_ev5 | 2085 | 39.6 | 41.0 | $-1397.46 | -6.7% | $-397.46 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2528 | 50.3 | 51.0 | $-1613.89 | -6.4% | $-613.89 | -3.3 | done | losing for real |
| coinflip | 4292 | 50.5 | 50.3 | $-1702.15 | -4.0% | $-702.15 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 4292 | 51.0 | 51.5 | $-2113.51 | -4.9% | $-1113.51 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3016 | 48.7 | 50.3 | $-2129.19 | -7.1% | $-1129.19 | -3.9 | done | losing for real |
| always_up | 4292 | 47.3 | 49.4 | $-3778.34 | -8.8% | $-2778.34 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6788 | 48.4 | 49.0 | $-3503.96 |
| ETH | 7359 | 48.1 | 48.5 | $-4661.21 |
| SOL | 7758 | 48.1 | 48.5 | $-4546.48 |
| XRP | 7838 | 48.3 | 48.3 | $-4591.08 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
