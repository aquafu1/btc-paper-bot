# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 8:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1251 windows, 33912 settled trades, 419 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 665 | 34.1 | 35.3 | $-524.16 | -7.9% | $475.84 | -1.6 | done | can't tell from luck |
| value_ev10 | 1625 | 38.4 | 39.2 | $-910.67 | -5.6% | $89.33 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3399 | 50.8 | 50.3 | $-1102.03 | -3.2% | $-102.03 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2843 | 49.5 | 49.4 | $-1319.21 | -4.6% | $-319.21 | -2.5 | done | losing for real |
| value_ev5 | 2456 | 40.3 | 41.1 | $-1359.26 | -5.5% | $-359.26 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 2843 | 50.5 | 51.1 | $-1673.74 | -5.9% | $-673.74 | -3.2 | done | losing for real |
| trend_filter | 2006 | 48.8 | 50.4 | $-1697.35 | -8.5% | $-697.35 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3399 | 49.2 | 50.2 | $-2117.27 | -6.2% | $-1117.27 | -3.7 | done | losing for real |
| coinflip | 4892 | 50.0 | 50.1 | $-2217.12 | -4.5% | $-1217.12 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4892 | 50.3 | 51.4 | $-2924.95 | -6.0% | $-1924.95 | -4.3 | done | losing for real |
| always_up | 4892 | 47.8 | 49.3 | $-3627.12 | -7.4% | $-2627.12 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7985 | 48.0 | 48.9 | $-4806.67 |
| ETH | 8617 | 48.1 | 48.3 | $-5082.00 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
