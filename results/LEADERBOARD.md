# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 1:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 742 windows, 20455 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 385 | 33.2 | 34.9 | $-352.66 | -9.2% | $647.34 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2096 | 51.7 | 50.7 | $-459.73 | -2.2% | $540.27 | -1.0 | done | can't tell from luck |
| value_ev10 | 934 | 37.8 | 39.1 | $-659.20 | -7.1% | $340.80 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1724 | 49.8 | 49.5 | $-691.97 | -4.0% | $308.03 | -1.7 | done | can't tell from luck |
| value_ev5 | 1412 | 40.3 | 41.1 | $-812.43 | -5.8% | $187.57 | -1.8 | done | can't tell from luck |
| trend_filter | 1204 | 49.7 | 50.9 | $-827.67 | -6.9% | $172.33 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1724 | 50.2 | 51.3 | $-1167.11 | -6.8% | $-167.11 | -2.9 | done | losing for real |
| coinflip | 2960 | 50.3 | 50.3 | $-1185.78 | -4.0% | $-185.78 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2096 | 48.3 | 50.1 | $-1562.60 | -7.5% | $-562.60 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2960 | 50.7 | 51.8 | $-1690.46 | -5.7% | $-690.46 | -3.2 | done | losing for real |
| always_up | 2960 | 47.0 | 49.6 | $-2755.88 | -9.3% | $-1755.88 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4633 | 48.1 | 49.1 | $-2975.34 |
| ETH | 5098 | 48.0 | 48.5 | $-3319.22 |
| SOL | 5331 | 48.0 | 48.6 | $-3221.28 |
| XRP | 5393 | 48.5 | 48.5 | $-2649.65 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
