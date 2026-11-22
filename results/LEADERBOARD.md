# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 12:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1074 windows, 29730 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 554 | 34.3 | 35.1 | $-353.30 | -6.4% | $646.70 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3014 | 51.3 | 50.5 | $-767.73 | -2.5% | $232.27 | -1.4 | done | can't tell from luck |
| value_ev10 | 1371 | 37.6 | 39.2 | $-999.47 | -7.3% | $0.53 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2528 | 49.7 | 49.6 | $-1151.47 | -4.6% | $-151.47 | -2.3 | done | losing for real |
| trend_filter | 1769 | 49.5 | 50.7 | $-1276.23 | -7.2% | $-276.23 | -3.1 | done | losing for real |
| value_ev5 | 2085 | 39.6 | 41.0 | $-1397.46 | -6.7% | $-397.46 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2528 | 50.3 | 51.0 | $-1613.89 | -6.4% | $-613.89 | -3.3 | done | losing for real |
| coinflip | 4289 | 50.5 | 50.3 | $-1692.87 | -3.9% | $-692.87 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 4289 | 51.0 | 51.5 | $-2083.51 | -4.9% | $-1083.51 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3014 | 48.7 | 50.3 | $-2147.64 | -7.1% | $-1147.64 | -4.0 | done | losing for real |
| always_up | 4289 | 47.2 | 49.4 | $-3807.51 | -8.9% | $-2807.51 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6788 | 48.4 | 49.0 | $-3503.96 |
| ETH | 7354 | 48.1 | 48.5 | $-4649.52 |
| SOL | 7753 | 48.1 | 48.5 | $-4535.07 |
| XRP | 7835 | 48.3 | 48.3 | $-4602.53 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
